from django.urls import path

from posts.views import (PostCreateView, PostDetailView, PostListView,
                         PostUpdateView, post_deleted)

app_name = 'posts'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('posts', PostListView.as_view(), name='posts'),
    path('posts_user/<int:pk>/', PostListView.as_view(), name='post_user'),
    path('page/<int:page>/', PostListView.as_view(), name='paginator'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('deleted/<int:user_id>/<int:post_id>/', post_deleted, name='post_deleted'),
]
