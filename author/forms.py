from django import forms
   
class CreateAuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email =  forms.EmailField(label=u"Votre adresse mail")
    avatar = forms.ImageField()

class ChangeAvatarForm(forms.Form):
	avatar = forms.ImageField()

