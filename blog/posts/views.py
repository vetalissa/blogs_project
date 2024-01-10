from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from posts.forms import PostForm
from posts.models import Post
from users.models import User


class HomeView(TitleMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    title = 'Блог'
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-date_create')[:3]


class PostCreateView(TitleMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    title = 'Создать пост'

    def get_success_url(self):
        return reverse_lazy('posts:post_user', args=(self.object.user.id,))

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


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('posts:post', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data()
        context['title'] = self.object.title_name
        context['post'] = self.object
        return context


def post_deleted(request, user_id, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect(reverse_lazy('posts:post_user', args=(user_id,)))
