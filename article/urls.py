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

from article import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/$', views.view_article, name="detail"),
	url(r'^(?P<article_id>\d+)/edit/$', views.edit_article, name="edit"),
	url(r'^new/$', views.edit_article, name="new"),
    url(r'^(?P<pk>\d+)/comments/$', views.view_comments, name="comments"),
)
