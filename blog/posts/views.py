from django.contrib.auth.views import TemplateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from posts.forms import PostCreateForm
from posts.models import Post
from users.models import User


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


class PostMixin(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/posts.html'
    ordering = ('-date_create')
    paginate_by = 3


class PostListView(TitleMixin, PostMixin):
    title = 'Все посты'


class PostUserListView(PostMixin):
    def get_queryset(self):
        queryset = super(PostUserListView, self).get_queryset()
        return queryset.filter(user=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUserListView, self).get_context_data(**kwargs)
        context['tile_username'] = User.objects.filter(pk=self.kwargs['pk']).get().username
        context['title'] = f'Блог {User.objects.filter(pk=self.kwargs["pk"]).get().username}'
        return context


class PostView(TitleMixin, DetailView):
    model = Post
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['title'] = self.object.title_name
        return context
