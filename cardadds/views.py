from django import forms
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.views import PasswordChangeView
from cardadds.models import CardAdd, BackgroundImage, CardCategory
from .forms import CardAddForm
from django.urls import reverse_lazy
# Create your views here.


@login_required()
def home(request):
    cards = CardAdd.objects.all()
    cats = CardCategory.objects.all()
    context = {
        "title": "card list",
        "cards": cards,
        "categories": cats
    }
    return render(request, "home.html", context)


@login_required()
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
                                 'Card successfully created name: %s.' % (instance.business_name))
            return redirect('cards:update-card', instance.ref_code)
    else:
        cardform = CardAddForm(request.POST or None, request.FILES or None)
    context = {
        "title": "create card",
        "form": cardform,
        "themes": themes
    }
    return render(request, "create_card.html", context)


def card_link(request, *args, **kwargs):
    card_code = kwargs.get('ref_code')
    data = get_object_or_404(CardAdd, ref_code=card_code)
    context = {
        "title": "card details",
        "instance": data,
        "baseURL": "http://localhost:8000"
    }
    return render(request, "card_link.html", context)


@login_required()
def update_card(request, ref_code):
    instance = get_object_or_404(CardAdd, ref_code=ref_code)
    form = CardAddForm(request.POST or None,
                       request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Card successfully updated name: %s.' % (instance.business_name))
        return redirect("cards:update-card", instance.ref_code)
    context = {
        "title": "card update",
        "instance": instance,
        "form": form
    }
    return render(request, "update_card.html", context)


@login_required()
def delete_card(request, *args, **kwargs):
    card_code = kwargs.get('ref_code')
    data = get_object_or_404(CardAdd, ref_code=card_code)
    if request.method == "POST":
        data.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Card successfully deleted.')
        return redirect('cards:home')
    context = {
        "title": "delete",
        "instance": data
    }
    return render(request, "delete.html", context)
