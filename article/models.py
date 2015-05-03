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
from member.models import Member

class Article(models.Model):
    event = models.ForeignKey(Event)
    author = models.ForeignKey(Member)
    is_beta = models.BooleanField()
    introduction = models.TextField()
    def __unicode__(self):
        return self.event.name
    def get_absolute_url(self):
        return '/article/' + str(self.pk) + '/'

    def get_edit_url(self):
        return '/article/' + str(self.pk) + '/edit/'

    def get_comment_url(self):
        return '/article/' + str(self.pk) + '/comments/'

    def get_as_dict(self):
        returned = {}
        returned['event'] = self.event.pk
        returned['author'] = self.author.pk
        returned['is_beta'] = self.is_beta
        returned['pk'] = self.pk
        #returned['parts'] = []
        #for p in self.parts:
        #    returned['parts'].append(p.pk)
        return returned
    def load_from_dict(self, d):
        if 'event' in d:
            self.event = Event.objects.get(pk=d['event'])
        if 'author' in d:
            self.author = Author.objects.get(pk=d['author'])
        if 'is_beta' in d:
            self.is_beta = d['is_beta']
        if 'pk' in d:
            self.pk = d['pk']


class Part(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200)
    article = models.ForeignKey(Article, related_name='parts')
    def __unicode__(self):
        return self.title
    def get_as_dict(self):
        returned = {}
        returned['text'] = self.text
        returned['title'] = self.title
        returned['article'] = self.article.pk
        return returned
    def load_from_dict(self, d):
        if 'text' in d:
            self.text = d['text']
        if 'title' in d:
            self.title = d['title']
        if 'article' in d:
            self.article = Article.objects.get(pk=d['article'])

class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, related_name='comments')
    member = models.ForeignKey(Member, related_name='comments')
    def __unicode__(self):
        return self.text
