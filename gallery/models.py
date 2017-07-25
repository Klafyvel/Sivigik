from django.db import models
from article.models import Article

import os

ATTACHEMENT_TYPE = (
    ('IMG', 'Image'),
    ('FILE', 'Fichier'),
)


class Attachment(models.Model):

    def get_upload_to(self, filename):
        return os.path.join('article',str(self.article.pk), 'attachments', filename)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    attachment_type = models.CharField(
        max_length=30,
        choices=ATTACHEMENT_TYPE,
        default='FILE')
    file = models.FileField(upload_to=get_upload_to, null=True)
    image = models.ImageField(upload_to=get_upload_to, null=True)

    def __str__(self):
        return str(self.attachment_type) + " de " + str(self.article)
