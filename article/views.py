from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


from .models import Article, URL_TO_CATEGORY, URL_TO_CATEGORY_NAME, URL_TO_DESCRP

class IndexView(generic.ListView):
    template_name = 'article/listArticles.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 20

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

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)

        with self.object.file.storage.open(self.object.file, 'r') as f:
            context['text'] = f.read()
        return context


class AuthorView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('author:ask_login')

    template_name = 'article/author.html'
    model = Article
    context_object_name = 'articles'


class EditView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('author:ask_login')

    template_name = 'article/edit.html'
    model = Article
    fields = ['authors', 'title', 'file', 'category', 'pub_date', 'is_beta']
    success_url = reverse_lazy('article:author')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)

        context['images'] = self.object.attachement_set.filter(attachement_type='IMG')
        context['files'] = self.object.attachement_set.filter(attachement_type='FILE')
        return context

    def post(self, request, **kwargs):
        if "save" in request.POST:
            self.success_url = reverse('article:edit', kwargs={'pk':self.get_object().pk})
        return super(EditView, self).post(request, **kwargs)

def new_article(request):
    a = Article()
    a.pub_date = timezone.now()
    a.title = "Nouvel article"
    a.save()
    return HttpResponseRedirect(reverse('article:edit', kwargs={'pk':a.pk}))


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('author:ask_login')
    model = Article
    success_url = reverse_lazy('article:author')
    template_name = "article/delete.html"