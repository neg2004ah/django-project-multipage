from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

def Login(request) :
    if request.user.is_authenticated:
        return redirect('/')
    
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else :
            messages.add_message(request, messages.ERROR , 'username or password is not valid ! ...')
            return redirect('accounts:login')


@login_required
def Logout(req) :
    logout(req)
    return redirect('/')


def signup(req):
    if req.method == 'GET':
        form = SignUpForm()
        return render(req, 'registration/signup.html', {'form': form})
    
    elif req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
