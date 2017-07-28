# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "author"
urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='author/login.html'), name='login'),
    url(r'^logout/$', views.logOut, name='logout'),
]