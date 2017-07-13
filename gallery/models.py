from django.db import models
from article.models import Article

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return "Image de "+ str(self.article)
