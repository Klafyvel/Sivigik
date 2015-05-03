from django.contrib import admin

from member.models import Member



class MemberAdmin(admin.ModelAdmin):
    fields=['user', 'avatar', 'is_author']

admin.site.register(Member, MemberAdmin)