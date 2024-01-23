from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import render

from comments.forms import CommentForm
from comments.models import Commment
from posts.models import Post


class CommentCreateView(CreateView):
    model = Commment
    template_name = 'comments/comments.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('posts:post', args=(self.kwargs['post_id'],))

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super(CommentCreateView, self).form_valid(form)


def comments(request, post):
    comments = Commment.objects.filter(post=post).order_by('-date_create')
    paginator = Paginator(comments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return page_obj
