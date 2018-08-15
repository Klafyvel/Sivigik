# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings

import os
import shutil

from .models import Article, URL_TO_CATEGORY, URL_TO_CATEGORY_NAME, URL_TO_DESCRP

class CategoryView(generic.ListView):
    """
    Display the articles in a given category.
    """
    template_name = 'article/category.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs.get('category')
        if context['category']:
            context['category_descpr'] = URL_TO_DESCRP[context['category']]
            context['category_name'] = URL_TO_CATEGORY_NAME[context['category']]
        return context

    def get_queryset(self):
        return Article.objects.filter(is_beta=False).filter(
            category=URL_TO_CATEGORY[self.kwargs.get('category')]
        ).order_by('-pub_date')


class IndexView(generic.ListView):
    """
    Display the latest article.
    """
    template_name = 'article/home.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(is_beta=False).order_by('-pub_date')[:10]


class ArticleView(generic.DetailView):
    """
    Display an article.
    """
    template_name = 'article/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)

        with self.object.file.storage.open(self.object.file, 'r') as f:
            context['text'] = f.read()
        return context

    def get_queryset(self):
        """
        An article can be accessed by its pk or its pub_date + slug.
        """
        allow_beta = self.request.user.is_authenticated
        if not allow_beta:
            search = {
                'is_beta': False
            }
        else:
            search = {}
        if 'pk' in self.kwargs :
            search['pk'] = self.kwargs['pk']
        else:
            search['year'] = self.kwargs['year']
            search['month'] = self.kwargs['month']
            search['slug'] = self.kwargs['slug']
        return Article.objects.filter(**search)


class AuthorView(LoginRequiredMixin, generic.ListView):
    """
    Display every article for authors.
    """
    login_url = reverse_lazy('author:login')

    template_name = 'article/author.html'
    model = Article
    context_object_name = 'articles'

    queryset = Article.objects.order_by('-pub_date')


class EditView(LoginRequiredMixin, generic.UpdateView):
    """
    Edit an article.
    """
    login_url = reverse_lazy('author:login')

    template_name = 'article/edit.html'
    model = Article
    fields = ['authors', 'title', 'file', 'category', 'pub_date', 'is_beta']
    success_url = reverse_lazy('article:author')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)

        context['images'] = self.object.attachment_set.filter(attachment_type='IMG')
        context['files'] = self.object.attachment_set.filter(attachment_type='FILE')
        return context

    def post(self, request, **kwargs):
        if "save" in request.POST:
            self.success_url = reverse('article:edit', kwargs={'pk':self.get_object().pk})
        return super(EditView, self).post(request, **kwargs)

def new_article(request):
    """
    Create an article then redirect the user to the edit page.
    """
    a = Article()
    a.pub_date = timezone.now()
    a.title = "Nouvel article"
    a.save()
    directory = os.path.join(settings.MEDIA_ROOT, a.get_upload_to(''))
    a.file.name = a.get_upload_to('article.md')
    file_path = os.path.join(settings.MEDIA_ROOT, a.file.name)
    os.mkdir(directory)
    with open(file_path, 'w+') as f:
        f.write("Nouvel article.")
    a.save()
    return HttpResponseRedirect(reverse('article:edit', kwargs={'pk':a.pk}))


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Delete an article.
    """
    login_url = reverse_lazy('author:login')
    model = Article
    success_url = reverse_lazy('article:author')
    template_name = "article/delete.html"

@login_required(login_url='/login/')
def make_archive(request, pk):
    """
    Create an archive of an article then redirect the user to it.
    """
    a = get_object_or_404(Article, pk=pk)
    archive = a.archive()
    return HttpResponseRedirect('/media/archive/'+archive)

@login_required(login_url='/login/')
def save_site(request):
    """
    Create an archive from every article then redirect the user to it.
    """
    for a in Article.objects.all():
        a.archive()
    dest = os.path.join(settings.MEDIA_ROOT, 'site')
    shutil.make_archive(dest, 'zip', settings.ARCHIVE_ROOT)
    return  HttpResponseRedirect('/media/site.zip')
