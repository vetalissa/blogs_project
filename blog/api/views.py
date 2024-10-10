from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializers


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        try:
            if request.data['author'] == request.user.username:
                obj = Post.objects.create(title_name=request.data['title_name'],
                                          description=request.data['description'], author=request.user)
                serializer = self.get_serializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'You can create post only with yourself username'},
                                status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(
                {
                    "title_name": ["Обязательное поле."],
                    "description": ["Обязательное поле."],
                    "author": ["Обязательное поле."]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs['pk'])
        if post.exists():
            post = post.first()
            if post.author == request.user:
                post.delete()
                return Response({'Delete': f'post {kwargs["pk"]} delete'}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'You can delete post only with yourself username'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': 'This ID wrong'},
                            status=status.HTTP_400_BAD_REQUEST)
