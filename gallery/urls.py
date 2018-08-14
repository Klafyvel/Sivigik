# coding: utf-8
from __future__ import unicode_literals
from django.urls import path

from gallery.views import *

app_name = "gallery"
urlpatterns = [
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:pk>)/', DeleteView.as_view(), name='delete'),
    path('new_image/<int:article_pk>/', new_image, name='new_image'),
    path('new_file/<int:article_pk>/', new_file, name='new_file'),
]
