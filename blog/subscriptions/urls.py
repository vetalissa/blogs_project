from django.urls import path

from subscriptions.views import create_follow_sub, delete_unfollow_sub

app_name = 'subscriptions'

urlpatterns = [
    path('follow/<int:user_sub>/<int:user_follow>/', create_follow_sub, name='follow'),
    path('unfollow/<int:user_sub>/<int:user_follow>/', delete_unfollow_sub, name='unfollow'),
]
