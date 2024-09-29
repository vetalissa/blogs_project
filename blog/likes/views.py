from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

from likes.models import Like, UserLike


@login_required
def click_for_like(request, user_id, post_id):
    user_like = UserLike.objects.filter(post_id=post_id, user_id=user_id)
    post_like = Like.objects.filter(post=post_id)

    if user_like.exists():
        user_like = user_like.last()
        post_like = post_like.first()

        post_like.count_like -= 1
        post_like.save()

        user_like.delete()
    else:
        UserLike.objects.create(post_id=post_id, user_id=user_id)
        post_like = post_like.first() if post_like.exists() else Like.objects.create(post_id=post_id)
        post_like.count_like += 1
        post_like.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
