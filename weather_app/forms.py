from django import forms
from django.forms import PasswordInput
from .models import CustomUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'password': PasswordInput(attrs={'type': 'password'}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']
        widgets = {
            'password': PasswordInput(attrs={'type': 'password'}),
        }
