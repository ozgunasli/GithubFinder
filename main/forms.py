from django import forms

class AramaForm(forms.Form):

    githubname = forms.CharField(max_length=100, label='Kullanıcı Adı')

