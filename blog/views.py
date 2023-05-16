from django.shortcuts import render
from django.utils import timezone
from .models import *
from advertisment.models import *
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


def blog_home(request,tag = None,username = None,cat = None):
    posts = Post.objects.filter(status= True,published_date__lte = timezone.now())
    category = Category.objects.all()
    tags = Tags.objects.all()
    last_four_posts = posts[:4]
    adv = AdvertisModel.objects.all()[0]
    
    if tag:
        posts = Post.objects.filter(tag__name = tag)
        
    if username:
        posts = Post.objects.filter(author__username = username)
    
    if cat:
        posts = Post.objects.filter(category__name = cat)
    
    if request.GET.get('search'):
        posts = Post.objects.filter(content__contains = request.GET.get('search'))
        
    
    posts = Paginator(posts,3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    
    context = {
        'posts' : posts,
        'category' : category,
        'tags' : tags,
        'last_four_posts' : last_four_posts,
        'ADV' : adv,
    }
    return render(request , 'blog/blog-home.html',context = context)







def blog_single(request):
    return render(request , 'blog/blog-single.html')