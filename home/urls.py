from django.urls import *
from .views import *



urlpatterns = [
    path('',home),
    path('about',about),
    path('blog-single',blog_single),
    path('blog-home',blog_home),
    path('contact',contact),
    path('elements',elements),
]
