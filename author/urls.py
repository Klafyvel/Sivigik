# coding: utf-8
from __future__ import unicode_literals
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "author"
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='author/login.html'), name='login'),
    path('logout/', views.logOut, name='logout'),
]
