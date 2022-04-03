from django.forms import ModelForm
from django import forms

from articleapp.models import Article


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'height:auto; text-left;'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']