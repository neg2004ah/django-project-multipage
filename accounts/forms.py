from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email','image','id_code']