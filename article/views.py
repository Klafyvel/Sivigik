from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Article, URL_TO_CATEGORY, URL_TO_CATEGORY_NAME, URL_TO_DESCRP

class IndexView(generic.ListView):
    template_name = 'article/listArticles.html'
    context_object_name = 'articles'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['is_category'] = (len(self.args) > 0)
        if context['is_category']:
            context['category'] = self.args[0]
            context['category_descpr'] = URL_TO_DESCRP[self.args[0]]
            context['category_name'] = URL_TO_CATEGORY_NAME[self.args[0]]
        return context

    def get_queryset(self):
        if len(self.args) == 0 : # Main page
            return Article.objects.filter(is_beta=False).order_by('-pub_date')[:5]
        else : # Category page
            return Article.objects.filter(is_beta=False).filter(category=URL_TO_CATEGORY[self.args[0]]).order_by('-pub_date')

class ArticleView(generic.DetailView):
    template_name = 'article/detail.html'
    model = Article


class AuthorView(generic.ListView):
    template_name = 'article/author.html'
    model = Article
    context_object_name = 'articles'


class EditView(generic.UpdateView):
    template_name = 'article/edit.html'
    model = Article
    fields = ['authors', 'title', 'file', 'category', 'pub_date', 'is_beta']
    success_url = reverse_lazy('article:author')