from django.urls import path

from subscriptions.views import (FollowViewList, SubViewList,
                                 create_follow_sub, delete_unfollow_sub)

app_name = 'subscriptions'

urlpatterns = [
    path('follow/<int:user_sub>/<int:user_follow>/', create_follow_sub, name='follow'),
    path('unfollow/<int:user_sub>/<int:user_follow>/', delete_unfollow_sub, name='unfollow'),
    path('sub-list/<int:author_page>/', SubViewList.as_view(), name='sub_list'),
    path('follow-list/<int:author_page>/', FollowViewList.as_view(), name='follow_list'),
]
