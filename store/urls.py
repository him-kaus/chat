from django.urls import path
from . import views
from .views import register,home,login,profile,chatroom,logout

urlpatterns = [
    path('', home,name='home'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('profile',profile,name='profile'),
    path('chatroom',chatroom,name='chatroom')
]
