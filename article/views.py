from django.shortcuts import render, get_object_or_404

from django.views import generic

from article.models import Article

#import markdown

def view_article(request, article_id):
    a = get_object_or404(Article, pk=article_id)
    d = {'event_name' : a.event.name, 
         'text' : self.text
        }
    #return render(request, 'article/detail.html'

class DetailView(generic.DetailView):
	model = Article
	template_name = "article/detail.html" 
	#context_object_name = 'article'


