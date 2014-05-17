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
