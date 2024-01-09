from django.forms import ModelForm

from posts.models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title_name', 'description')
