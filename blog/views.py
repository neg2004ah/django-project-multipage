from django.shortcuts import render
from django.utils import timezone
from .models import *


def blog_home(request):
    posts = Post.objects.filter(status= True,published_date__lte = timezone.now())
    
    context = {
        'posts' : posts
    }
    return render(request , 'blog/blog-home.html',context = context)

def blog_single(request):
    return render(request , 'blog/blog-single.html')