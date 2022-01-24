from django.contrib.auth import get_user_model, forms
from django import forms

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    widget = forms.PasswordInput()
    attrs = {
        "class": "form-control",
        "id": "user-password"
    }
