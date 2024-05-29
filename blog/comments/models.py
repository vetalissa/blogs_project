from django.db import models

from posts.models import Post
from users.models import User


class Commment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField(max_length=200)
