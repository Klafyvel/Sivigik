from django import forms

from article.models import Article
from home.models import Event

class EditForm(forms.Form):
    image = forms.ImageField()
    pub_date=forms.DateTimeField()
    author = forms.ModelChoiceField(queryset=Article.objects.all())
    category = forms.ModelsChoiceField(queryset=Event.objects.all())
    is_beta = forms.BooleanField(default=True)
    text = forms.CharField(widget=forms.Textarea)
    
