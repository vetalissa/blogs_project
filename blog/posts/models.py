from django.db import models

from users.models import User


class Post(models.Model):
    title_name = models.CharField(max_length=100)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
