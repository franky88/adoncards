from django import forms
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from cardadds.models import CardAdd
from .forms import CardAddForm
# Create your views here.


def home(request):
    cards = CardAdd.objects.all()
    context = {
        "title": "card list",
        "cards": cards
    }
    return render(request, "home.html", context)


def create_card(request):
    if not request.user.is_authenticated:
        return redirect('cards:home')
    cardform = CardAddForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if cardform.is_valid():
            instance = cardform.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect('cards:home')
    else:
        cardform = CardAddForm(request.POST or None, request.FILES or None)
    context = {
        "title": "create card",
        "form": cardform
    }
    return render(request, "create_card.html", context)


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
