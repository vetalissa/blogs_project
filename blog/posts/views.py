from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from comments.views import comments
from common.views import TitleMixin
from likes.models import Like, UserLike
from posts.forms import PostForm
from posts.models import Post
from subscriptions.models import Subscription
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
        return reverse_lazy('posts:post_user', args=(self.object.author.id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostListView(TitleMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/posts.html'
    ordering = ('-date_create',)
    paginate_by = 3
    title = 'Все посты'


class PostUserListView(PostListView):
    def get_queryset(self):
        queryset = super(PostUserListView, self).get_queryset()
        author_id = self.kwargs.get('pk')
        return queryset.filter(author_id=author_id) if author_id else queryset

    def get_context_data(self, **kwargs):
        context = super(PostUserListView, self).get_context_data()

        author_id = self.kwargs['pk'] if self.kwargs else ''

        if author_id:
            author_page = User.objects.get(id=author_id)

            context['author_page'] = author_page
            context['count_following'] = Subscription.object.count_following(author_page)
            context['count_subscription'] = Subscription.object.count_subscription(author_page)
            context['title'] = f' Посты {author_page.username}'
            if self.request.user.is_authenticated is True:
                context['check_sub'] = Subscription.object.check_sub(self.request.user, author_page)
        else:
            context['title'] = 'Все посты'

        return context


class PostSubListView(PostListView):
    title = 'Посты подписки'

    def get_queryset(self):
        queryset = super(PostSubListView, self).get_queryset()
        author_id = self.kwargs.get('pk')
        list_sub = [i.user_follow for i in Subscription.object.filter(user_sub_id=author_id)]
        return [post for post in queryset if post.author in list_sub]


class PostDetailView(TitleMixin, DetailView):
    model = Post
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        context['title'] = self.object.title_name
        context['comment'] = comments(self.request, self.object)

        like_post = Like.objects.filter(post_id=self.object)
        context['count_like'] = like_post.get(post=self.object).count_like if like_post.exists() else 0

        like_user = UserLike.objects.filter(user_id=self.request.user.id, post=self.object)
        context['like_user'] = True if like_user.exists() else False

        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        if check_user(request, kwargs['pk']) is False:
            return redirect('home')
        else:
            return super(PostUpdateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('posts:post', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data()
        context['title'] = self.object.title_name
        return context


@login_required
def post_deleted(request, user_id, post_id):
    post = check_user(request, post_id)
    if post is False:
        return redirect('home')
    else:
        post.delete()
        return redirect(reverse_lazy('posts:post_user', args=(user_id,)))


def check_user(request, post_id):
    post = Post.objects.filter(id=post_id)
    if post.exists() and request.user == post.first().author:
        return post.first()
    return False
