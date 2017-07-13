from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from article.models import Article
from .models import Image

class EditView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('author:ask_login')

    template_name = 'gallery/edit.html'
    model = Image
    fields = ['image']

    def get_success_url(self, **kwargs):
        if self.success_url :
            return self.success_url
        return reverse('gallery:new', kwargs={'article_pk':self.object.article.pk})

    def post(self, request, **kwargs):
        print(request)
        if 'cancel' in request.POST:
            return HttpResponseRedirect(reverse('gallery:delete', 
                kwargs={'pk':self.get_object().pk}))
        elif 'save_and_quit' in request.POST:
            self.success_url = reverse('article:edit', kwargs={'pk':self.get_object().article.pk})
        return super(EditView, self).post(request, **kwargs)

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('author:ask_login')
    model = Image
    template_name = "article/delete.html"
    def get_success_url(self, **kwargs):
        return reverse('article:edit', kwargs={'pk':self.object.article.pk})


def new_image(request, article_pk):
    image = Image()
    image.article = get_object_or_404(Article, pk=article_pk)
    image.save()
    return HttpResponseRedirect(reverse('gallery:edit', kwargs={'pk':image.pk}))