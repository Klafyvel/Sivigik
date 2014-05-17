from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime

from home.models import Category
from article.models import Article

class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.filter(is_beta=False)

    def lastmod(self, obj):
        return obj.event.pub_date

class BaseSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return ['/']

    def location(self, obj):
        return obj

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    def location(self, item):
        return '/category/'+ item.name
