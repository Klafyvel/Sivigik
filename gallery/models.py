from django.db import models
from article.models import Article


class Gallery(models.Model):
    article = models.OneToOneField(Article)

    def __str__(self):
        return self.article.title


class Image(models.Model):
    gallery = models.ForeignKey(Gallery)
    image = models.ImageField()
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=500)
