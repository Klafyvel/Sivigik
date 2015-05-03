#This file is part of Sivigik.
#
#Foobar is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Foobar is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
from django.conf.urls import patterns, url

from member import views

urlpatterns = patterns('',
    url(r'^login/$', views.connect, name='login'),
    url(r'^logout/$', views.disconnect, name='logout'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^articles/$', views.article_list, name='articles_list'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^create_author/$', views.create_author, name='create_author'),
    url(r'^change_avatar/$', views.change_avatar, name='change_avatar'),
    url(r'^static_pages/$', views.static_pages_list, name='static_pages_list'),
)