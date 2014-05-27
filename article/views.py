#This file is part of Sivigik.
#
#Foobar is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Foobar is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.views import generic

from article.models import Article
from home.models import Event

from article.forms import EditArticleForm

from django.utils import timezone

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

@login_required(login_url='/author/login/')
def edit_article(request, article_id=0):
    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES)

        if form.is_valid():

            author = request.user.author
            date = timezone.now()
            title = form.cleaned_data['title']
            is_beta = form.cleaned_data['is_beta']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']

            if article_id == 0:
            	e = Event(name=title, pub_date=date, category=category, image=None)

            	a = Article(event=e, author=author, is_beta=is_beta, text=text)
            else:
            	a = get_object_or_404(Article, pk=article_id)
            	if image is None:
            		image = a.event.image
            	e = a.event
            	a.author = author
            	a.is_beta = is_beta
            	a.text = text
            	e.name = title
            	e.pub_date = date
            	e.category = category
            	e.image = image
            	a.event = e

            e.save()
            a.save()



            return HttpResponseRedirect(a.get_absolute_url())
    else:
    	if article_id == 0:
        	form = EditArticleForm()
        else:
        	a = get_object_or_404(Article, pk=article_id)
    		form = EditArticleForm(initial={'title':a.event.name,
    										'image':a.event.image,
    										'category':a.event.category,
    										'is_beta':a.is_beta,
    										'text':a.text})
    if article_id == 0:
    	send_to = '/article/new/'
    else :
    	send_to = '/article/edit/' + article_id + '/'
    
    return render(request, 'article/edit.html', locals())