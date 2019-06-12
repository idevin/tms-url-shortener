from django import forms
from django.core import validators


class MainForm(forms.Form):
    url = forms.URLField(label=False, validators=[validators.URLValidator()])


class HashForm(forms.Form):
    hash = forms.RegexField(
        label=False,
        validators=[validators.RegexValidator],
        regex=r'[0-9a-zA-Z\s]+'
    )
