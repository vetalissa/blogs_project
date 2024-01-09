from django.urls import path

from posts.views import (PostCreateView, PostListView, PostUserListView,
                         PostView)

app_name = 'posts'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('page/<int:page>/', PostListView.as_view(), name='paginator'),
    path('posts_user/<int:pk>/', PostUserListView.as_view(), name='post_user'),
    path('page/<int:page>/', PostUserListView.as_view(), name='paginator'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
]
