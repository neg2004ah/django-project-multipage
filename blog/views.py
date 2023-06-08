from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.utils import timezone
from .models import *
from .forms import *
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


def blog_single(request,pid):
    
    if request.method == 'GET':
        post_list_id = []
        posts = Post.objects.filter(status = True)
        
        for post in posts:
            post_list_id.append(post.id)
            
        post_list_id.reverse()
                
        if post_list_id.index(pid) == 0:
            previous_post = None
            next_post = posts.get(id=post_list_id[1])
            
        elif post_list_id.index(pid) == post_list_id.index(post_list_id[-1]):
            previous_post = posts.get(id = post_list_id[-2])
            next_post = None
        else:
            next_post = posts.get(id = post_list_id[post_list_id.index(pid) +1 ])
            previous_post = posts.get(id = post_list_id[post_list_id.index(pid) -1 ])
            
            
        try:
            comments = Comments.objects.filter(which_post=pid ,status = True)
            replay = Replay.objects.filter(status = True)
            post = Post.objects.get(id=pid,status = True)
            posts = Post.objects.filter(status= True,published_date__lte = timezone.now())
            last_four_posts = posts[:4]
            post.counted_views += 1
            post.save()
            
            context = {
                'post' : post,
                'last_four_posts' : last_four_posts,
                'next' : next_post,
                'previous' : previous_post,
                'comments': comments,
                'replay' : replay,
            }
            return render(request , 'blog/blog-single.html',context=context)
        except:
            return render(request,'blog/404.html')
        
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        
        
        
def replay(request, cid):
     comment = Comments.objects.get(id=cid)
     if request.method == 'GET':
          context = {
               'comment' : comment,
          }
          return render(request, 'blog/reply.html', context=context)   
     
     elif request.method == 'POST':
          form = ReplayForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
           
           
           
           
def delete(request, cid):
     comment = Comments.objects.get(id=cid)
     comment.delete()
     return redirect('/')   
     
     
     

def edit(request, cid):
     comment = Comments.objects.get(id=cid)
     if request.method == 'GET':
          
          form = CommentForm(instance=comment)
          context = {
               'form' : form,
          }
          return render(request,'blog/commentedit.html',context=context)
      
     elif request.method == "POST" :
          form = CommentForm(request.POST, instance=comment)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
           
           
           
def add(request):
     if request.method == 'GET':
          context = {
               'form' : PostForm()
          }
          return render(request,'blog/add.html',context=context)
      
     elif request.method == 'POST':
          form = PostForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               return redirect('/blog/')
