from django.contrib.auth.decorators import login_required
from django.urls import path

from posts.views import (PostCreateView, PostDetailView, PostListView,
                         PostSubListView, PostUpdateView, PostUserListView,
                         post_deleted)

app_name = 'posts'

urlpatterns = [
    path('create/', login_required(PostCreateView.as_view()), name='create'),
    path('update/<int:pk>/', login_required(PostUpdateView.as_view()), name='post_update'),
    path('posts', PostListView.as_view(), name='posts'),
    path('posts-user/<int:pk>/', PostUserListView.as_view(), name='post_user'),
    path('posts-user-sub/<int:pk>/', PostSubListView.as_view(), name='post_user_sub'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('deleted/<int:user_id>/<int:post_id>/', post_deleted, name='post_deleted'),
]
