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
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views import generic

#from author.forms import ConnectForm
from author.models import Author
from article.models import Article

def connect(request):
    return login(request, template_name="author/login.html")

@login_required(login_url='/author/login/')
def disconnect(request):
    return logout(request, next_page='/', template_name='author/logout.html')

@login_required(login_url='/author/login/')
def set_password(request):
    return password_change(request, template_name='author/set_password.html', post_change_redirect='/author/profil')

@login_required(login_url='/author/login/')
def  profil(request):
    return render(request, 'author/profil.html')

@login_required(login_url='/author/login/')
def article_list(request):
    if request.user.username is not None: 
        my_author = request.user.author
        return render(request, 'author/article_list.html', {'author':my_author})
    else:
        return disconnect(request)
    
