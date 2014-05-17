#-*- coding:utf-8 -*-
from django import template
from random import randint

from home.models import Category

register = template.Library()

@register.tag
def categories(parser, token):
    """ Tag renvoyant la liste des catégories formattée."""
    return CategoryListNode()


class CategoryListNode(template.Node):
    def __init__(self):
        self.cat_list = Category.objects.all()
        self.formated_list = str()
        for c in self.cat_list:
             self.formated_list += u'<li><a href=\'/category/' + str(c.name) + u'\'>' + str(c.displayed_name) + u'</a></li>\n'

    def render(self, context):
           return self.formated_list
