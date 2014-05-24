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

#-*- coding:utf-8 -*-
from django import template
from random import randint

from home.models import Category

register = template.Library()

@register.tag
def categories(parser, token):
    return CategoryListNode()


class CategoryListNode(template.Node):
    def __init__(self):
        self.cat_list = Category.objects.all()
        self.formated_list = str()
        for c in self.cat_list:
             self.formated_list += u'<li><a href=\'/category/' + str(c.name) + u'\'>' + str(c.displayed_name) + u'</a></li>\n'

    def render(self, context):
           return self.formated_list
