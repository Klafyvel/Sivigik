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
#-*-coding:utf-8-*-

#def add_page_to_sitemap(url):
#    file_content =''
#    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'r') as file:
#        file_content = file.read()
#
#    file_content = file_content.replace('</urlset>', '\n')
#    file_content += '<url><loc>' + url + '</loc></url>\n</urlset>'
#
#    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'w') as file:
#        file.write(file_content)

import json
from article.models import Article, Part
from author.models import Author
from home.models import Category, Event, GoodSite

def save_json_site():
    site = {}
    site['Article'] = [a.get_as_dict() for a in Article.objects.all()]
    site['Part'] = [p.get_as_dict() for p in Part.objects.all()]
    site['Author'] = [a.get_as_dict() for a in Author.objects.all()]
    site['Category'] = [c.get_as_dict() for c in Category.objects.all()]
    site['Event'] = [e.get_as_dict() for e in Event.objects.all()]
    site['GoodSite'] = [g.get_as_dict() for g in GoodSite.objects.all()]
    with open('save.json', 'w') as f:
        json.dump(site, f, indent=4)

