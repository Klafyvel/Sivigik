from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.forms import modelform_factory

from article.models import Article
from .models import Attachment

class EditView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('author:ask_login')

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
    login_url = reverse_lazy('author:ask_login')
    model = Attachment
    template_name = "article/delete.html"
    def get_success_url(self, **kwargs):
        return reverse('article:edit', kwargs={'pk':self.object.article.pk})


def new_image(request, article_pk):
    image = Attachment()
    image.article = get_object_or_404(Article, pk=article_pk)
    image.attachment_type = 'IMG'
    image.save()
    return HttpResponseRedirect(reverse('gallery:edit', kwargs={'pk':image.pk}))


def new_file(request, article_pk):
    file = Attachment()
    file.article = get_object_or_404(Article, pk=article_pk)
    file.attachment_type = 'FILE'
    file.save()
    return HttpResponseRedirect(reverse('gallery:edit', kwargs={'pk':file.pk}))