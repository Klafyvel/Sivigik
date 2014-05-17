from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from django.utils import timezone

class Author(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")    
    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)

    def get_article_list(self):
        articles = []
        for a in self.article_set.all():
            articles.append(a)
        return articles

    def get_latest_articles(self):
        articles = []
        for a in self.article_set.all().filter(is_beta=False):
            if a.event.pub_date < timezone.now():
                articles.append(a)
        return articles
