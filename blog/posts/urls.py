from django.urls import path

from posts.views import PostCreateView, PostListView, PostView

app_name = 'posts'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('paginate/<int:page>/', PostListView.as_view(), name='paginate'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
]
