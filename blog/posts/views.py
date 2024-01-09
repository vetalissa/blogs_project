from django.contrib.auth.views import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from posts.forms import PostCreateForm
from posts.models import Post


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


class PostListView(TitleMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    title = 'Все посты'
    template_name = 'posts/posts.html'
    ordering = ('-date_create')
    paginate_by = 3
