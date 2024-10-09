from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializers


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
