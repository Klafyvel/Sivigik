from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

import shutil
import os
import json

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

    def get_upload_to(self, filename):
        return os.path.join('article',str(self.pk),filename)

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
        self.slug = slugify(self.title)
        self.month = self.pub_date.month
        self.year = self.pub_date.year
        super(Article, self).save(*args, **kwargs)

    def meta_json(self):
        data = {
            "authors": [a.username for a in self.authors.all()],
            "title": self.title,
            "category": self.category,
            "pub_date": self.pub_date.timestamp(),
            "is_beta": self.is_beta,
        }
        return json.dumps(data)

    def archive(self):
        archive_path = os.path.join(settings.ARCHIVE_ROOT, self.slug)
        try:
            os.remove(archive_path)
        except FileNotFoundError:
            pass
        directory = os.path.join(settings.ARCHIVE_ROOT, self.slug, '')
        shutil.copytree(os.path.join(settings.MEDIA_ROOT,self.get_upload_to('')), directory)

        with open(os.path.join(directory, 'meta.json'), 'w') as f:
            f.write(self.meta_json())

        shutil.make_archive(archive_path, 'zip', directory)

        shutil.rmtree(directory)

        return self.slug + '.zip'