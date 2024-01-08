from django.shortcuts import render
from django.urls import reverse_lazy

from common.views import TitleMixin
from django.contrib.auth.views import TemplateView
from django.views.generic.edit import CreateView

from posts.models import Post
from posts.forms import PostCreateForm


class HomeView(TitleMixin, TemplateView):
    title = 'Блог'
    template_name = 'posts/index.html'


class PostCreateView(TitleMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    title = 'Создать пост'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
