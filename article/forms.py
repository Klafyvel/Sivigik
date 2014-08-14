# -*- coding: utf-8 -*-
from django import forms

from home.models import Category

class EditArticleForm(forms.Form):
    error_css_class = 'error'

    title = forms.CharField(max_length=200, label=u'Titre :')
    image = forms.ImageField(required=False, label=u'Image :')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label=u'Catégorie :')
    is_beta = forms.BooleanField(label=unicode(u'Cet article est en bêta :'), required=False)
    is_pinned = forms.BooleanField(label=unicode(u'Épingler cet article sur la page d\'accueil :'), required=False)
    text = forms.CharField(widget=forms.Textarea, label='Texte :')

