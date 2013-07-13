__author__ = 'tbsmith'
from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
