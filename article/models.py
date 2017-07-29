# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

import shutil
import os
import sys
import json
import uuid

CATEGORIES = (
    ('EXP', 'Expériences et bricolages'),
    ('PROJ', 'Projets'),
    ('BAZ', 'Bazar de Sivigik'),
    ('PROG', 'Programmation'),
    ('SITE', 'Vie du site'),
)

URL_TO_CATEGORY_NAME = {
    'exp': 'Expériences et bricolages',
    'projets': 'Projets',
    'bazar': 'Bazar de Sivigik',
    'programmation': 'Programmation',
    'site': 'Vie du site',
}

URL_TO_CATEGORY = {
    'exp': 'EXP',
    'projets': 'PROJ',
    'bazar': 'BAZ',
    'programmation': 'PROG',
    'site': 'SITE',
}

URL_TO_DESCRP = {
    'exp': "Nous regroupons ici nos expériences et nos très petits projets, Enjoy !",
    'projets': 'Voici nos projets de plus grandes envergure.',
    'bazar': "Ici il y a tous nos articles qui ne rentrent pas dans une autre catégorie.",
    'programmation': "Nos articles de programmation.",
    'site': "Les informations à propos du site.",
}


class Article(models.Model):
    """
    Model for an article.
    """

    def get_upload_to(self, filename):
        """
        Return the location of the markdown file.
        """
        if filename:
            return os.path.join('article',str(self.pk),str(uuid.uuid1())+'-'+filename)
        else:
            return os.path.join('article',str(self.pk),'')

    authors = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=1000, default="")
    file = models.FileField(upload_to=get_upload_to, null=True)
    category = models.CharField(
        max_length=30,
        choices=CATEGORIES,
        default='SITE',
    )
    pub_date = models.DateTimeField(
        'Date de publication', default=timezone.now)
    is_beta = models.BooleanField(default=True)

    slug = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overwrite the slug, month, year to match with title and pub_date, then save the article.
        """
        self.slug = slugify(self.title)
        self.month = self.pub_date.month
        self.year = self.pub_date.year
        super(Article, self).save(*args, **kwargs)

    def meta_json(self):
        """
        Return metadata in a JSON string.
        """
        data = {
            "authors": [a.username for a in self.authors.all()],
            "title": self.title,
            "category": self.category,
            "pub_date": self.pub_date.isoformat(),
            "is_beta": self.is_beta,
        }
        return json.dumps(data)

    def archive(self):
        """
        Create an archive of the article.
        Archive looks like :
        .
        |- article.md
        |- meta.json
        |- attachments
            | - files and images...

        Return the name of the archive.
        """
        archive_path = os.path.join(settings.ARCHIVE_ROOT, self.slug+'_'+str(self.pk))
        if sys.version_info[0] >= 3:
            try:
                os.remove(archive_path)
            except FileNotFoundError:
                pass
        else:
            try:
                os.remove(archive_path)
            except OSError:
                pass
        directory = os.path.join(settings.ARCHIVE_ROOT, self.slug, '')
        shutil.copytree(os.path.join(settings.MEDIA_ROOT,self.get_upload_to('')), directory)

        with open(os.path.join(directory, 'meta.json'), 'w') as f:
            f.write(self.meta_json())

        shutil.make_archive(archive_path, 'zip', directory)

        shutil.rmtree(directory)

        return self.slug + '_' + str(self.pk) + '.zip'


@receiver(models.signals.post_delete, sender=Article)
def delete_file_at_delete(sender, instance, **kwargs):
    """
    Delete the article folder in /media/ after the article was deleted.
    """
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, instance.get_upload_to('')))

    archive_path = os.path.join(settings.ARCHIVE_ROOT, instance.slug + '_' + str(instance.pk) + '.zip')
    if os.path.isfile(archive_path):
        os.remove(archive_path)


@receiver(models.signals.pre_save, sender=Article)
def delete_file_on_update(sender, instance, **kwargs):
    """
    Delete the old article file when uploading a new one.
    """
    if not instance.pk:
        return False
    try:
        old_file = Article.objects.get(pk=instance.pk).file
    except Article.DoesNotExist:
        return False

    if old_file:
        if (old_file != instance.file) and os.path.isfile(old_file.path):
            os.remove(old_file.path)