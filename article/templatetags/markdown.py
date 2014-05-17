# -*- coding:utf-8 -*-
from django import template

import os
import random

register = template.Library()

@register.filter(is_safe=True)
def markdown(text):
    """Parse the given markdown text in html."""
    returned_html = str()
    tmp_file_name = 'tmp_' + str(random.randint(0, 1000)) + '.md'

    with open(tmp_file_name, 'w') as tmp_file:
        tmp_file.write(text.encode('utf-8'))
    
    pandoc_command = 'pandoc --asciimath --toc -f markdown -t html -i ' + tmp_file_name
    returned_html = os.popen(pandoc_command).read()
    os.system(str('rm -f ' + tmp_file_name))

    return returned_html
