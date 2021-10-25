from django import forms
from django.forms import fields
from .models import CardAdd
from django.forms import RadioSelect, widgets, TextInput


class CardAddForm(forms.ModelForm):
    class Meta:
        model = CardAdd
        fields = [
            # "category",
            "business_name",
            "title",
            "content",
            "promotion",
            "business_reinstatement",
            "image"
        ]
        # widgets = {
        #     'image': RadioSelect(attrs={'type': 'radio'})
        # }
