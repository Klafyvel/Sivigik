from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='index'),
    url(r'^(?P<category_name>[A-Za-z]+)/$', views.category, name='category'),
)
