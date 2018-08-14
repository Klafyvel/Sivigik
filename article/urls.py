# coding: utf-8
from __future__ import unicode_literals
from django.urls import path

from article.views import *

app_name = "article"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', ArticleView.as_view(), name='article-detail-pk'),
    path('<int:year>/<int:month>/<slug:slug>', ArticleView.as_view(), name='article-detail-wp'),
    path('categorie/<str>/', IndexView.as_view(), name='article-category'),
    path('page-auteurs/', AuthorView.as_view(), name='author'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('new/', new_article, name='new'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('archive/<int:pk>', make_archive, name='archive'),
    path('save_site', save_site, name='save_site'),
]
