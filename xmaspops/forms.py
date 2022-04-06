from dataclasses import field
from pyexpat import model
from django import forms
from django.forms.widgets import TextInput
from .models import PopUp, Theme
from django.forms import widgets


class PopUpForms(forms.ModelForm):
    class Meta:
        model = PopUp
        fields = [
            'business_name',
            'content',
            'title',
            'reinstatement',
            'text_color',
            'theme'
        ]
        widgets = {
            'content': widgets.Textarea(attrs={'rows': '3'}),
            'reinstatement': widgets.Textarea(attrs={'rows': '3'}),
            'text_color': TextInput(attrs={"type": "color"}),
        }


class ThemeForms(forms.ModelForm):
    class Meta:
        model = Theme
        fields = [
            'name',
            'image',
        ]
