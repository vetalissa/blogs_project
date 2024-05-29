from django.forms import ModelForm

from comments.models import Commment


class CommentForm(ModelForm):
    class Meta:
        model = Commment
        fields = ('comment_text',)
