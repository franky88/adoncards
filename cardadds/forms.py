from django import forms
from django.forms import fields
from .models import CardAdd, CardCategory
from django.forms import RadioSelect, widgets, TextInput, Textarea


class CardAddForm(forms.ModelForm):
    error_css_class = 'error-field'
    # required_css_class = 'required-field'
    business_name = forms.CharField(max_length=50, help_text='50 characters max.',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Content title', max_length=40, help_text='40 characters max.', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(max_length=100, help_text='100 characters max.', required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3'}))
    closing_content = forms.CharField(max_length=80, help_text='80 characters max.', required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    promotion_content = forms.CharField(max_length=100, help_text='100 characters max.', required=False,
                                        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    promotional_offer = forms.CharField(max_length=20, help_text='20 characters max.', required=False,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    business_reinstatement = forms.CharField(max_length=100, help_text='100 characters max.', required=False,
                                             widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = CardAdd
        fields = [
            # "category",
            "business_name",
            "title",
            "content",
            "closing_content",
            "promotion_content",
            "promotional_offer",
            "business_reinstatement",
            "image"
        ]
