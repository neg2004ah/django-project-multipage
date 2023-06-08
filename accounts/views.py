from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .models import CustomUser

def Login(request) :
    if request.user.is_authenticated:
        return redirect('/')
    
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
                username = user.username

            except CustomUser.DoesNotExist:
                messages.add_message(request, messages.ERROR , "User with this email does not exist.")
                return redirect('accounts:login')
            
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else :
            messages.add_message(request, messages.ERROR , 'username or password is not valid ! ...')
            return redirect('accounts:login')


@login_required
def Logout(request) :
    logout(request)
    return redirect('/')



def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    elif request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else :
            messages.add_message(request, messages.ERROR , 'input value is not valid ! ...')
            return redirect('accounts:signup')
    
    