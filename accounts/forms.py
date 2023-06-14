from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import CustomUser
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()


    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email','image','id_code','captcha']
        
        
        


class CaptchaForm(forms.Form):
    captcha = CaptchaField()