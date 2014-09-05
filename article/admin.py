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
from django.contrib import admin

from article.models import Article, Part

class PartInline(admin.StackedInline):
    model = Part

class ArticleAdmin(admin.ModelAdmin):
    inlines=[PartInline]

class ArticleInline(admin.StackedInline):
	model = Article
	extra = 1
	max_num = 1
admin.site.register(Part)
admin.site.register(Article, ArticleAdmin)
