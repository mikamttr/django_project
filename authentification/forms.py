from django import forms
from authentification.models import User


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=50, label='username')
        password = forms.CharField(max_length=60, widget=forms.PasswordInput, label='mot de passe')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
