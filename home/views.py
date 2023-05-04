from django.shortcuts import render
from .models import *

def home (request):
    cheap = CheapPackages.objects.all()
    luxury = LuxuryPackages.objects.all()
    camping = CampingPackages.objects.all()
    
    context = {
        'cheap' : cheap , 
        'luxury' : luxury,
        'camping' :camping,
    }
    
    return render(request,'home/index.html',context = context)



def contact (request):
    return render(request,'home/contact.html')

def elements (request):
    return render(request,'home/elements.html')

def about (request):
    return render(request,'home/about.html')
