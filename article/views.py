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


