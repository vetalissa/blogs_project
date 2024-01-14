from django.urls import path

from comments.views import CommentCreateView

app_name = 'comments'

urlpatterns = [
    path('comments-create/<int:post_id>/', CommentCreateView.as_view(), name='create_comment'),
]
