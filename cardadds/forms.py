from django import forms
from django.forms import fields
from .models import CardAdd


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
