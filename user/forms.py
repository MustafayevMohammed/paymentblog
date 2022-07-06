from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    username = forms.CharField(required=True)
    email = forms.EmailField(required=True,widget=forms.EmailInput)
    password1 = forms.CharField(required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(required=True,widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]


class LoginForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput)
    password = forms.CharField(required=True,widget=forms.PasswordInput)
