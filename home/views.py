from django.shortcuts import render,redirect
from .forms import NewsletterForm
from blog.models import *
from .models import *

def home (request):
    if request.method == 'GET':
        cheap = CheapPackages.objects.all()
        luxury = LuxuryPackages.objects.all()
        camping = CampingPackages.objects.all()
        
        last_six_posts = Post.objects.filter(status = True)[:6]
        
        context = {
            'cheap' : cheap , 
            'luxury' : luxury,
            'camping' :camping,
            'last_six_posts' : last_six_posts
        }
        
        return render(request,'home/index.html',context = context)
    
    elif request.method == 'POST':
        new = Newsletter()
        form = NewsletterForm(request.POST)
        if form.is_valid():
            new.email = request.POST.get('email')
            new.save()
        return redirect('/')
        


def contact (request):
    return render(request,'home/contact.html')

def elements (request):
    return render(request,'home/elements.html')

def about (request):
    return render(request,'home/about.html')
