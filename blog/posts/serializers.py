from rest_framework import serializers

from posts.models import Post
from users.models import User


class PostSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title_name', 'description', 'date_create', 'author']
        read_only_fields = ('date_create',)
