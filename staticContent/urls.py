from django.conf.urls import patterns, url

from staticContent import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.static_content_view, name="content"),
    url(r'^(?P<pk>\d+)/style/$', views.static_content_style_view, name="content_style"),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_static_content, name="edit"),
    url(r'^new/$', views.edit_static_content, name="edit"),
)