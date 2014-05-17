from django.contrib import admin

from author.models import Author



class AuthorAdmin(admin.ModelAdmin):
    fields=['user', 'avatar']

admin.site.register(Author, AuthorAdmin)
