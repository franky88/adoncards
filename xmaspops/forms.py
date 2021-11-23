from django import forms
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
            'theme'
        ]
        widgets = {
            'content': widgets.Textarea(attrs={'rows': '3'}),
            'reinstatement': widgets.Textarea(attrs={'rows': '3'}),
        }
