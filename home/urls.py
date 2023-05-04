from django.urls import *
from .views import *

app_name = 'home'


urlpatterns = [
    path('',home,name = 'home'),
    path('about',about,name ='about'),
    path('contact',contact,name = 'contact'),
    path('elements',elements,name = 'elements'),
]
