from django.urls import path

from likes.views import click_for_like

app_name = 'likes'

urlpatterns = [
    path('post/like/<int:user_id>/<int:post_id>/', click_for_like, name='click_for_like'),
]
