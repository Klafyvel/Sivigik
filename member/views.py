from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

from django.views import generic

from member.forms import CreateAuthorForm#, ChangeAvatarForm
from member.models import Member
from article.models import Article

def connect(request):
    return login(request, template_name="member/login.html")

@login_required(login_url='/member/login/')
def disconnect(request):
    return logout(request, next_page='/', template_name='member/logout.html')

@login_required(login_url='/member/login/')
def set_password(request):
    return password_change(request, template_name='member/set_password.html', post_change_redirect='/member/profil')

@login_required(login_url='/member/login/')
def  profil(request):
    return render(request, 'member/profil.html')

@login_required(login_url='/member/login/')
def article_list(request): 
    the_member = request.user.member
    return render(request, 'member/article_list.html', {'member':the_member})

@login_required(login_url='/member/login/')
def change_avatar(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES)

        if form.is_valid():

            avatar = form.cleaned_data['avatar']

            request.user.member.avatar = avatar
            request.user.member.save()

            changed = True
    else:
        form = ChangeAvatarForm()

    return render(request, 'member/change_avatar.html', locals())

@login_required(login_url='/member/login/')
def static_pages_list(request):
    the_member = request.user.member
    return render(request, 'member/static_pages_list.html', {'member':the_member})

@permission_required('is_superuser')
def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST, request.FILES)

        if form.is_valid():

            the_member = form.cleaned_data['member']

            the_member.is_author = True
            the_member.save()

            created = True
    else:
        form = CreateAuthorForm()

    return render(request, 'member/create_author.html', locals())
    
