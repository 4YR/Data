from django import forms
from .models import People


class AddDataForm(forms.Form):
    name = forms.CharField(required=True)
    address = forms.CharField(required=False)