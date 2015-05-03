from django.db import models
from member.models import Member

class StaticContent(models.Model):
    content = models.TextField()
    style = models.TextField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Member)
    def __unicode__(self):
        return self.title
