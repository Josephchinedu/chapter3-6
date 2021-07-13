from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=PasswordInput())