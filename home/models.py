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
from django.db import models

import datetime
from django.utils import timezone
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=200)
    displayed_name = models.CharField(max_length=200)
    comment = models.TextField()
    def __unicode__(self):
        return self.name + " : " + self.comment


class Event(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publication')
    category = models.ForeignKey(Category)
    image = models.ImageField(null=True, blank=True, upload_to="imgArticles/")
    is_pinned = models.BooleanField()
    def __unicode__(self):
        return self.name
    def get_as_dict(self):
        returned = {}
        returned['name'] = self.name
        returned['pub_date'] = self.pub_date.toordinal()
        returned['category'] = self.category.pk
        try:
            returned['image'] = self.image.file.name
        except ValueError:
            returned['image'] = ''
        returned['is_pinned'] = self.is_pinned
        returned['pk'] = self.pk
        return returned
    def load_from_dict(self, d):
        if 'name' in d:
            self.name = d['name']
        if 'pub_date' in d:
            self.pub_date = datetime.datetime.fromordinal(d['pub_date'])
        if 'category' in d:
            self.category = Category.objects.get(pk = d['category'])
        if 'image' in d:
            f = File(open(d['image']))
            self.image.save(f.name, f, save=False)
        if 'pk' in d:
            self.pk = d['pk']

class GoodSite(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name + " : " + self.comment

def get_pinned_events():
    """Returns the pinneds events."""
    return Event.objects.filter(is_pinned=True)[:2]

def get_latest_events():
    """ Returns the last published events."""
    return Event.objects.filter(pub_date__lte=timezone.now()).filter(article__is_beta=False).filter(is_pinned=False).order_by('-pub_date')[:4]

def get_events_by_category(category):
    returned_events = []
    for e in Event.objects.all().order_by('-pub_date'):
        if e.category == category and e.pub_date < timezone.now():
            returned_events.append(e)
    return returned_events

def get_good_sites():
    """Returns the good sites list."""
    return GoodSite.objects.all()

def get_category_by_name(category_name):
    for c in Category.objects.all():
        if c.name == category_name:
            return c

def get_beta_events():
    return Event.objects.all().filter(article__is_beta=True)
