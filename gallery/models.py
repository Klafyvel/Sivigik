from django.db import models
from article.models import Article


ATTACHEMENT_TYPE = (
    ('IMG', 'Image'),
    ('FILE', 'Fichier'),
)

class Attachement(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    attachement_type = models.CharField(
        max_length=30,
        choices=ATTACHEMENT_TYPE,
        default='FILE')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)

    def __str__(self):
        return str(self.attachement_type) + " de " + str(self.article)
