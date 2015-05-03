# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import formset_factory

from member.models import Member

class CreateMemberForm(forms.Form):
    
    error_css_class = 'error'
    pseudo = forms.CharField(max_length=200, label=u'Pseudo :')
    addr = forms.EmailField(label=u'Adresse mail (ne sera pas divulguée) :')
    password = forms.CharField(max_length=50, label=u"Mot de passe", widget=forms.PasswordInput)
    cond = forms.BooleanField(label=u"J'ai lu et j'accepte les conditions d'utilisation de sivigik")
