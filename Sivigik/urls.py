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
from django.conf.urls import patterns, include, url
from django.contrib import admin

from Sivigik.settings import IS_MAINTENANCE

from sitemap import *

admin.autodiscover()
sitemaps = {
    'main': BaseSitemap,
    'articles':ArticleSitemap,
    'category':CategorySitemap,
}

if IS_MAINTENANCE:
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('maintenance.urls', namespace='maintenance')),
)
else: 
    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'Sivigik.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
	    url(r'^article/', include('article.urls', namespace="article")),
        url(r'^admin/', include(admin.site.urls)),
	    url(r'^$', include('home.urls', namespace="home")),
	    url(r'^category/', include('home.urls', namespace="home")),
        url(r'^author/', include('author.urls', namespace="author")),
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    )

