from django import forms
from html2image import Html2Image
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from cardadds.models import CardAdd, BackgroundImage, CardCategory
from .forms import CardAddForm
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(request):
    cards = CardAdd.objects.all()
    cats = CardCategory.objects.all()
    context = {
        "title": "card list",
        "cards": cards,
        "categories": cats
    }
    return render(request, "home.html", context)


def create_card(request):
    if not request.user.is_authenticated:
        return redirect('cards:home')
    themes = BackgroundImage.objects.all()
    cardform = CardAddForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if cardform.is_valid():
            instance = cardform.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Card successfuly created %s.' % (instance.title))
            return redirect('cards:card-details', instance.ref_code)
    else:
        cardform = CardAddForm(request.POST or None, request.FILES or None)
    context = {
        "title": "create card",
        "form": cardform,
        "themes": themes
    }
    return render(request, "create_card.html", context)


def card_details(request, *args, **kwargs):
    card_code = kwargs.get('ref_code')
    instance = get_object_or_404(CardAdd, ref_code=card_code)
    context = {
        "title": "card details",
        "instance": instance,
        "baseURL": "http://localhost:8000"
    }
    return render(request, "detail_card.html", context)


def card_link(request, ref_code):
    instance = get_object_or_404(CardAdd, ref_code=ref_code)
    context = {
        "title": "card details",
        "instance": instance,
        "baseURL": "http://localhost:8000"
    }
    return render(request, "card_link.html", context)


def update_card(request, ref_code):
    instance = get_object_or_404(CardAdd, ref_code=ref_code)
    form = CardAddForm(request.POST or None,
                       request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("cards:home")
    context = {
        "title": "update card",
        "instance": instance,
        "form": form
    }
    return render(request, "update_card.html", context)


def users(request):
    users = User.objects.all()
    context = {
        "title": "users",
        "users": users
    }
    return render(request, "users.html", context)
