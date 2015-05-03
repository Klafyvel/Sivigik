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

# -*- coding:utf-8 -*-
from django import template
import markdown

register = template.Library()

extensions = ['markdown.extensions.extra', 
              'markdown.extensions.codehilite',
              'markdown.extensions.smarty',
              'markdown.extensions.mathjax',
             ]

extension_configs = {
    'CodeHilite' : {
        'linenums' : True,
        # 'linenos' : True,
        'use_pygments': False,
    },
}
md = markdown.Markdown(extensions, extension_configs)

@register.filter(is_safe=True)
def emarkdown(text):
    """Parse the given markdown text in html."""
    return md.convert(text)
