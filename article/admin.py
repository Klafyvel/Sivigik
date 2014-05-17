from django.contrib import admin

from article.models import Article

class ArticleInline(admin.StackedInline):
	model = Article
	extra = 1
	max_num = 1
admin.site.register(Article)
