from django import forms
from .models import ShortURL


class URLForm(forms.Form):
    long_url = forms.URLField(label='Enter URL', max_length=200, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your URL here'}))