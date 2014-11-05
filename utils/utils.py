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
from home.models import Category, Event

def save_json_site():
    site = {}
    site['Article'] = [a.get_as_dict() for a in Article.objects.all()]
    site['Part'] = [p.get_as_dict() for p in Part.objects.all()]
    site['Event'] = [e.get_as_dict() for e in Event.objects.all()]
    site['Category'] = [e.get_as_dict() for e in Category.objects.all()]
    site['Author'] = [e.get_as_dict() for e in Author.objects.all()]
    with open('save.json', 'w') as f:
        json.dump(site, f, indent=4)

def load_json_site(fic):
    site = {}
    with open(fic, 'r') as json_file:
        site = json.load(json_file)
    for a_json in site['Author']:
        try :
            a = Author.objects.get(pk=a_json['pk'])
        except:
            a = Author()
        a.load_from_dict(a_json)
        a.save()
    for a_json in site['Category']:
        try :
            a = Category.objects.get(pk=a_json['pk'])
        except:
            a = Category()
        a.load_from_dict(a_json)
        a.save()
    for a_json in site['Event']:
        try :
            a = Event.objects.get(pk=a_json['pk'])
        except:
            a = Event()
        a.load_from_dict(a_json)
        a.save()
    for a_json in site['Article']:
        try :
            a = Article.objects.get(pk=a_json['pk'])
        except:
            a = Article()
        a.load_from_dict(a_json)
        a.save()
    for a_json in site['Part']:
        try :
            a = Part.objects.get(pk=a_json['pk'])
        except:
            a = Part()
        a.load_from_dict(a_json)
        a.save()