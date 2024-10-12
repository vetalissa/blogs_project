from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthor
from posts.models import Post
from posts.serializers import PostSerializers
from users.models import User


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthor]

    def get_queryset(self):
        queryset = super().get_queryset()
        author_name = self.request.query_params.get('author', None)
        user = User.objects.filter(username=author_name)
        if user.exists():
            queryset = queryset.filter(author=user.first())
        return queryset
