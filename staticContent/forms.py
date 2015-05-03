# -*- coding: utf-8 -*-
from django import forms
from django.forms.formsets import formset_factory

from staticContent.models import StaticContent

class EditStaticContentForm(forms.Form):
    error_css_class = 'error'
    title = forms.CharField(max_length=200, label=u'Titre :')
    content = forms.CharField(widget=forms.Textarea, label='Html :')
    style = forms.CharField(widget=forms.Textarea, label='CSS :')
