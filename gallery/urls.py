# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import url

from gallery.views import *

app_name = "gallery"
urlpatterns = [
    url(r'^edit/(?P<pk>\d+)/$', EditView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteView.as_view(), name='delete'),
    url(r'^new_image/(?P<article_pk>\d+)/$', new_image, name='new_image'),
    url(r'^new_file/(?P<article_pk>\d+)/$', new_file, name='new_file'),
]