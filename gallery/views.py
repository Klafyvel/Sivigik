# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms import modelform_factory
from django.conf import settings

import os
import sys

from article.models import Article
from .models import Attachment

class EditView(LoginRequiredMixin, generic.UpdateView):
    """
    Edit an attachment.
    """
    login_url = reverse_lazy('author:login')

    template_name = 'gallery/edit.html'
    model = Attachment
    fields = []

    def get_success_url(self, **kwargs):
        if self.success_url :
            return self.success_url
        elif self.object.attachment_type == 'IMG':
            return reverse('gallery:new_image', kwargs={'article_pk':self.object.article.pk})
        else :
            return reverse('gallery:new_file', kwargs={'article_pk':self.object.article.pk})

    def post(self, request, **kwargs):
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('gallery:delete', 
                kwargs={'pk':self.get_object().pk}))
        elif 'save_and_quit' in request.POST:
            self.success_url = reverse('article:edit', kwargs={'pk':self.get_object().article.pk})
        return super(EditView, self).post(request, **kwargs)

    def get_form_class(self):
        if self.object.attachment_type == 'IMG':
            return modelform_factory(Attachment, fields=('image',))
        else:
            return modelform_factory(Attachment, fields=('file',))

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Delete an attachment.
    """
    login_url = reverse_lazy('author:login')
    model = Attachment
    template_name = "article/delete.html"
    def get_success_url(self, **kwargs):
        return reverse('article:edit', kwargs={'pk':self.object.article.pk})


def new_image(request, article_pk):
    """
    Create an image and redirect the user to the edit view.
    """
    image = Attachment()
    image.article = get_object_or_404(Article, pk=article_pk)
    image.attachment_type = 'IMG'
    image.save()
    directory = os.path.join(settings.MEDIA_ROOT, image.get_upload_to(''))
    image.image.name = image.get_upload_to('image.ppm')
    file_path = os.path.join(settings.MEDIA_ROOT, image.image.name)
    if sys.version_info[0] < 3 :
        try:
            os.mkdir(directory)
        except OSError:
            pass
    else:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
    with open(file_path, 'w+') as f:
        f.write("P1\n1 1\n0")
    image.save()
    return HttpResponseRedirect(reverse('gallery:edit', kwargs={'pk':image.pk}))


def new_file(request, article_pk):
    """
    Create a file and redirect the user to the edit view.
    """
    file = Attachment()
    file.article = get_object_or_404(Article, pk=article_pk)
    file.attachment_type = 'FILE'
    file.save()
    directory = os.path.join(settings.MEDIA_ROOT, file.get_upload_to(''))
    file.file.name = file.get_upload_to('fichier')
    file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    if sys.version_info[0] < 3 :
        try:
            os.mkdir(directory)
        except OSError:
            pass
    else:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
    with open(file_path, 'w+') as f:
        f.write("Un fichier")
    file.save()
    return HttpResponseRedirect(reverse('gallery:edit', kwargs={'pk':file.pk}))