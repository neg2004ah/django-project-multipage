from django.shortcuts import render
from .models import *


def blog_home(request):
    posts = Post.objects.filter(status = True)
    
    context = {
        'posts' : posts
    }
    return render(request , 'blog/blog-home.html',context = context)

def blog_single(request):
    return render(request , 'blog/blog-single.html')