from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='app'),
    path('deals', views.deals, name='deals'),
    path('iPhone13', views.iPhone13, name='iPhone13'),
    path('sonybravia', views.sonybravia, name='sonybravia'),
    path('applepro', views.applepro, name='applepro'),
    path('electronics', views.electronics, name='electronics'),
    path('fashion', views.fashion, name='fashion'),
    path('children', views.children, name='children'),
    path('women', views.women, name='women'),
    path('men', views.men, name='men'),
    path('signin', views.handleSignin, name="handleSignin"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('logout', views.handleLogout, name='handleLogout'),
    path('checkout', views.checkout, name='checkout'),
    path('tracker', views.tracker, name='tracker'),

    
]
