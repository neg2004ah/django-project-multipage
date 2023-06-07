from django.urls import *
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', signup, name='signup'),
]