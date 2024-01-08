from django.urls import path

from posts.views import PostCreateView

app_name = 'posts'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),

]
