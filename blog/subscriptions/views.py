from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

from subscriptions.models import Subscription


@login_required
def create_follow_sub(request, user_sub, user_follow):
    Subscription.object.follow_sub(user_sub, user_follow)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def delete_unfollow_sub(request, user_sub, user_follow):
    Subscription.object.unfollow_sub(user_sub, user_follow)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
