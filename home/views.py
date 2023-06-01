from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import NewsletterForm,ContactUsForm
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
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

def contact(request):
    if request.method == 'GET':
        return render(request,"home/contact.html")
    
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        

def elements (request):
    return render(request,'home/elements.html')

def about (request):
    return render(request,'home/about.html')
