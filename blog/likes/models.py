from django.db import models

from posts.models import Post
from users.models import User


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    count_like = models.PositiveIntegerField(default=0)


class UserLike(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
