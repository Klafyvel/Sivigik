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
