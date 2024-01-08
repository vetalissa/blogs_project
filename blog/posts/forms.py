from django import forms
from django.forms import ModelForm

from posts.models import Post


class PostCreateForm(ModelForm):
    # title_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-title'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'style': 'border: 1px solid black;', 'row':'15', 'cols':'80'}))

    class Meta:
        model = Post
        fields = ('title_name', 'description')
