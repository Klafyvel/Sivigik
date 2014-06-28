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
from django.test import TestCase

from django.core.urlresolvers import reverse

from article.models import Article

class ArticleMethodTest(TestCase):
	def test_get_absolute_url(self):
		a = Article()
		self.assertEqual(a.get_absolute_url(), '/article/' + str(a.id) + '/')
	def test_get_edit_url(self):
    	a = Article()
    	self.assertEqual(a.get_edit_url(), '/article/edit/' + str(a.id) + '/')

class ArticleViewTest(TestCase):
	def test_contains_text(self):
		pass
	def test_contains_author_name(self):
		pass
	def test_contains_event_title(self):
		pass
