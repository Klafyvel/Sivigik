from django.db import models
from django.core.files import File
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
    def get_five_last_articles(self):
        return self.get_latest_articles()[:3]
    def get_as_dict(self):
        r = {}
        r['user'] = {
            'username':self.user.username,
            'first_name':self.user.first_name,
            'last_name':self.user.last_name,
            'email':self.user.email,
            'password':self.user.password,
            'is_staff':self.user.is_staff,
            'is_superuser':self.user.is_superuser,
            'pk':self.user.pk
        }
        try:
            r['avatar'] = self.avatar.file.name
        except ValueError:
            r['avatar'] = ''
        return r
    def load_from_dict(self, d):
        if 'user' in d:
            try:
                u=User.objects.get(pk=d['user']['pk'])
            except:
                u = User()
            u.username = d['user']['username']
            u.first_name = d['user']['first_name']
            u.last_name = d['user']['last_name']
            u.email = d['user']['email']
            u.password = d['user']['password']
            u.is_staff = d['user']['is_staff']
            u.is_superuser = d['user']['is_superuser']
            u.pk = d['user']['pk']
            u.save()
            self.user = u
        if 'avatar' in d:
            try:
                f = File(open(d['avatar']))
                self.avatar.save(f.name, f, save=False)
            except:
                pass