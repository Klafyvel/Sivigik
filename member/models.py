from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from django.utils import timezone

class Member(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")
    is_author = models.BooleanField()

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)
