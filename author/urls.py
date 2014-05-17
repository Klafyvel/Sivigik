from django.conf.urls import patterns, url

from author import views

urlpatterns = patterns('',
    url(r'^login/$', views.connect, name='login'),
    url(r'^logout/$', views.disconnect, name='logout'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^articles/$', views.article_list, name='articles_list'),
    url(r'^set_password/$', views.set_password, name='set_password'),
)
