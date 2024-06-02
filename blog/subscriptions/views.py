from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView

from subscriptions.models import Subscription
from users.models import User


class SubMixinListView(ListView):
    template_name = 'subscriptions/sub_users.html'
    model = Subscription
    queryset = Subscription.object.all()
    ordering = ('-created',)
    paginate_by = 5


class SubViewList(SubMixinListView):

    def get_queryset(self):
        queryset = super(SubViewList, self).get_queryset()
        author_id = self.kwargs.get('author_page')
        return [i.user_follow for i in queryset.filter(user_sub_id=author_id)]

    def get_context_data(self, **kwargs):
        context = super(SubViewList, self).get_context_data()
        author_page = User.objects.get(id=self.kwargs.get('author_page'))
        context['title'] = f'Подписки у {author_page}'
        context['non_sub'] = f'Пользователь {author_page} ни на кого не подписан'
        context['author_page'] = author_page
        return context


class FollowViewList(SubMixinListView):

    def get_queryset(self):
        queryset = super(FollowViewList, self).get_queryset()
        author_id = self.kwargs.get('author_page')
        return [i.user_sub for i in queryset.filter(user_follow_id=author_id)]

    def get_context_data(self, **kwargs):
        context = super(FollowViewList, self).get_context_data()
        author_page = User.objects.get(id=self.kwargs.get('author_page'))
        context['title'] = f'Подписчики у {author_page}'
        context['non_sub'] = f'На автора {author_page} никто не подписан...'
        context['author_page'] = author_page
        return context


@login_required
def create_follow_sub(request, user_sub, user_follow):
    Subscription.object.follow_sub(user_sub, user_follow)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete_unfollow_sub(request, user_sub, user_follow):
    Subscription.object.unfollow_sub(user_sub, user_follow)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
