from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def logIn(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('article:index'))
        else:
            return HttpResponseRedirect(reverse('author:ask_login'))
    except KeyError:
        return HttpResponseRedirect(reverse('author:ask_login'))

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('article:index'))

def ask_for_login(request):
    return render(request, "author/login.html")