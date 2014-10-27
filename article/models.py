#This file is part of Sivigik.
#
#Foobar is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Foobar is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Foobar. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from home.models import Event
from author.models import Author

class Article(models.Model):
    event = models.ForeignKey(Event)
    author = models.ForeignKey(Author)
    is_beta = models.BooleanField()
    modifiers = models.ManyToManyField(Author, related_name='modifiers+')

    def get_absolute_url(self):
        return '/article/' + str(self.id) + '/'

    def get_edit_url(self):
        return '/article/edit/' + str(self.id) + '/'
    def get_as_dict(self):
        returned = {}
        returned['event'] = self.event.id
        returned['author'] = self.author.id
        returned['is_beta'] = self.is_beta
        returned['modifiers'] = []
        for m in self.modifiers.all():
            returned['modifiers'].append(m.id)
        #returned['parts'] = []
        #for p in self.parts:
        #    returned['parts'].append(p.id)
        return returned


class Part(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200)
    article = models.ForeignKey(Article, related_name='parts')
    def get_as_dict(self):
        returned = {}
        returned['text'] = self.text
        returned['title'] = self.title
        returned['article'] = self.article.id
        return returned
