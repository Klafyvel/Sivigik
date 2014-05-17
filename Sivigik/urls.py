from django.conf.urls import patterns, include, url
from django.contrib import admin

from sitemap import *

admin.autodiscover()
sitemaps = {
    'main': BaseSitemap,
    'articles':ArticleSitemap,
    'category':CategorySitemap,
}


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

