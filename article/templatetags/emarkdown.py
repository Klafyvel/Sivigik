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

import os
import random

import re
import markdown

single_dieses = re.compile(r'#+')
highest_level_title = re.compile(r'#\w*\r')
the_end = re.compile(r'\r')
line_regex = re.compile(r'\n')
title_level = [ re.compile(r'^#\w'),
                re.compile(r'^##\w'),
                re.compile(r'^###\w'),
                re.compile(r'^####\w'),
                re.compile(r'^#####\w'),
                re.compile(r'^######\w')]

extract_title_name = lambda t: the_end.sub('', single_dieses.sub('',t)) 

def compile_titles(title):
    if title_level[0].match(title):
        return '<h3 onclick="show(\'{0}\');">{0}</h3>\n'.format(extract_title_name(title))
    elif title_level[1].match(title):
        return '<h4>{}</h4>\n'.format(extract_title_name(title))
    elif title_level[2].match(title):
        return '<h5>{}</h5>\n'.format(extract_title_name(title))
    elif title_level[3].match(title):
        return '<h6>{}</h6>\n'.format(extract_title_name(title))
    elif title_level[4].match(title):
        return '<strong>{}</strong>\n'.format(extract_title_name(title))
    elif title_level[5].match(title):
        return '<strong>{}</strong>\n'.format(extract_title_name(title))

def parts_to_div(text):
    output = str()
    titles = highest_level_title.findall(text)
    print(titles)
    parts = highest_level_title.split(text)[1:]
    for t, p in zip(titles, parts):
        output += t + u'\n<div id=\'{}\' class=\'part\'>\n\n'.format(extract_title_name(t)) + markdown.markdown(p) + u'\n\n</div>\n'
    return output    

register = template.Library()

@register.filter(is_safe=True)
def emarkdown(text):
    """Parse the given markdown text in html."""
    first_preprocessed=parts_to_div(text)
    second_preprocessed = str()
    for l in line_regex.split(first_preprocessed):
        if single_dieses.match(l): 
            second_preprocessed += compile_titles(l)
        else:
            second_preprocessed += l
    print(second_preprocessed)
    return second_preprocessed

class JavascriptShowNode(template.Node):
    def __init__(self):
        pass
    def render(self, context):
        return """<script type="text/javascript">
    function show(id)
    {
        var obj=document.getElementById(id);
        if(obj.style.display == 'none')
        {
            obj.style.display='block';
        }
        else
        {
        obj.style.display='none';
        }
    }
</script>
"""

@register.tag()
def javascript_show(parser, token):
    return JavascriptShowNode()
    
