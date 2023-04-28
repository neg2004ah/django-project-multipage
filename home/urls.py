from django.urls import *
from .views import *

app_name = 'home'


urlpatterns = [
    path('',home,name = 'home'),
    path('about',about,name ='about'),
    path('blog-single',blog_single,name = 'blog_single'),
    path('blog-home',blog_home,name = 'blog_home'),
    path('contact',contact,name = 'contact'),
    path('elements',elements,name = 'elements'),
]
