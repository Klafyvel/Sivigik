# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from article.models import Article
from django.dispatch import receiver
from django.utils import timezone


import os
import uuid


ATTACHEMENT_TYPE = (
    ('IMG', 'Image'),
    ('FILE', 'Fichier'),
)


class Attachment(models.Model):
    """
    An attachment, can be a file or an image.
    """
    def get_upload_to(self, filename):
        """
        Return the location of the file.
        """
        if filename:
            return os.path.join('article',str(self.article.pk), 'attachments', str(uuid.uuid1())+'-'+filename)
        else:
            return os.path.join('article',str(self.article.pk),'attachments','')

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    attachment_type = models.CharField(
        max_length=30,
        choices=ATTACHEMENT_TYPE,
        default='FILE')
    file = models.FileField(upload_to=get_upload_to, null=True)
    image = models.ImageField(upload_to=get_upload_to, null=True)

    def __str__(self):
        return str(self.attachment_type) + " de " + str(self.article)


@receiver(models.signals.post_delete, sender=Attachment)
def delete_attachment_at_delete(sender, instance, **kwargs):
    """
    Delete the attachment file the attachment was deleted.
    """
    if instance.attachment_type == 'FILE':
        old_file = instance.file
    else:
        old_file = instance.image

    if old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=Attachment)
def delete_attachment_on_update(sender, instance, **kwargs):
    """
    Delete the old attachment file when uploading a new one.
    """
    if not instance.pk:
        return False
    try:
        if instance.attachment_type == 'FILE':
            old_file = Attachment.objects.get(pk=instance.pk).file
        else:
            old_file = Attachment.objects.get(pk=instance.pk).image
    except Attachment.DoesNotExist:
        return False
        
    if old_file:
        if instance.attachment_type == 'FILE':
            if (old_file != instance.file) and os.path.isfile(old_file.path):
                os.remove(old_file.path)
        else:
            if (old_file != instance.image) and os.path.isfile(old_file.path):
                os.remove(old_file.path)