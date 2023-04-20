from django.shortcuts import render

def home (request):
    return render(request,'home/index.html')

def blog_home (request):
    return render(request,'home/blog-home.html')

def blog_single (request):
    return render(request,'home/blog-single.html')

def contact (request):
    return render(request,'home/contact.html')

def elements (request):
    return render(request,'home/elements.html')

def about (request):
    return render(request,'home/about.html')
