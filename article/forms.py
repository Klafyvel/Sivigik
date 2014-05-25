#-*-coding : utf-8-*-
from django import forms

from home.models import Category

class EditArticleForm(forms.Form):
	title = forms.CharField(max_length=200)
	image = forms.ImageField()
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	is_beta = forms.BooleanField(help_text=u'Cette article est en beta.')
	text = forms.CharField(widget=forms.Textarea)
