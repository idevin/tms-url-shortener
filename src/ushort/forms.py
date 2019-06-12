from django import forms
from django.core import validators


class MainForm(forms.Form):
    url = forms.URLField(label=False, validators=[validators.URLValidator()])
