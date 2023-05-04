from django.urls import *
from .views import *

app_name = 'blog'

urlpatterns = [
    path("",blog_home , name="blog_home"),
    path("blog_single",blog_single , name="blog_single"),
]
