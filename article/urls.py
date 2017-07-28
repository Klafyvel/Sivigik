# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import url

from article.views import *

app_name = "article"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ArticleView.as_view(), name='article-detail-pk'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>(\w|-)+)/$', ArticleView.as_view(), name='article-detail-wp'),
    url(r'^categorie/(\w+)/$', IndexView.as_view(), name='article-category'),
    url(r'^page-auteurs/$', AuthorView.as_view(), name='author'),
    url(r'^edit/(?P<pk>\d+)/$', EditView.as_view(), name='edit'),
    url(r'^new/$', new_article, name='new'),
    url(r'^delete/(?P<pk>\d+)$', DeleteView.as_view(), name='delete'),
    url(r'^archive/(?P<pk>\d+)$', make_archive, name='archive'),
    url(r'^save_site/$', save_site, name='save_site'),
]