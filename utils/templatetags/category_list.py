# This file is part of Sivigik.
#
# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

#-*- coding:utf-8 -*-
from django import template
from random import randint

from home.models import Category

register = template.Library()


@register.simple_tag
def categories(current=None, show_beta=False, style="desktop"):
    if current == None:
        s = -3
    else:
        s = current
    r = '\n'
    css = ""
    if style is "desktop":
        css = ""
    else :
        css = "button maximized_small_screen"

    if current == -1:
        r += "<li> <a class='%s current_category' href=\"/\">Accueil</a></li>\n"%css
    else:
        r += "<li><a class='%s' href=\"/\">Accueil</a></li>\n"%css

    for c in Category.objects.all():
        if c.pk == s:
            r += "<li><a class='%s current_category' href='/categories/"%css + \
                str(c.name) + "'>" + str(c.displayed_name) + u'</a></li>\n'
        else:
            r += "<li><a class='%s' href='/categories/"%css + \
                str(c.name) + "'>" + str(c.displayed_name) + u'</a></li>\n'
    if show_beta and current == -2:
        r += "<li> <a class='%s current_category' href=\"/categories/beta/\">Articles en b&ecirc;ta</a></li>\n"%css
    elif show_beta:
        r += "<li> <a class='%s' href=\"/categories/beta/\">Articles en b&ecirc;ta</a></li>\n"%css

    return r
