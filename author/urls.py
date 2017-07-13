from django.conf.urls import url

from . import views

app_name = "author"
urlpatterns = [
    url(r'^$', views.ask_for_login, name='ask_login'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^logout/$', views.logOut, name='logout'),
]