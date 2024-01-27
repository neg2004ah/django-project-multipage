from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import CustumUser
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()


    class Meta:
        model = CustumUser
        fields = ['username', 'password1', 'password2', 'email','captcha']


class CaptchaForm(forms.Form):
    captcha = CaptchaField()