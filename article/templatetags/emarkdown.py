# coding: utf-8
from __future__ import unicode_literals
from django import template
import markdown

register = template.Library()

extensions = ['markdown.extensions.extra', 
              'markdown.extensions.codehilite',
              'markdown.extensions.toc',
              'mdx_math',
             ]

extension_configs = {
    'CodeHilite' : {
        'linenums' : True,
        'use_pygments': True,
    },
}
md = markdown.Markdown(extensions, extension_configs)

@register.filter(is_safe=True)
def emarkdown(text):
    """Parse the given markdown text in html."""
    return md.convert(text)