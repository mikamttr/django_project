from django import forms
from authentification.models import User


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=50, label='username')
        password = forms.CharField(max_length=60, widget=forms.PasswordInput, label='mot de passe')


class UserForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=50, label='username')
        password = forms.CharField(max_length=60, widget=forms.PasswordInput, label='mot de passe')
        user_role = forms.CharField(max_length=20, label='role')
        email = forms.CharField(max_length=60, label='email')
