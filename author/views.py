# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('article:index'))