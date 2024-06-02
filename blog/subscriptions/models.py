from django.db import models

from users.models import User


class SubQuerySet(models.QuerySet):

    def count_following(self, user_follow):
        return self.filter(user_follow=user_follow).count()

    def count_subscription(self, user_sub):
        return self.filter(user_sub=user_sub).count()

    def follow_sub(self, user_sub, user_follow):
        if not self.check_sub(user_sub=user_sub, user_follow=user_follow):
            user_sub = User.objects.get(id=user_sub)
            user_follow = User.objects.get(id=user_follow)
            self.create(user_sub=user_sub, user_follow=user_follow)

    def unfollow_sub(self, user_sub, user_follow):
        user_sub = User.objects.get(id=user_sub)
        user_follow = User.objects.get(id=user_follow)
        obj = self.filter(user_sub=user_sub, user_follow=user_follow)
        obj.delete()

    def check_sub(self, user_sub, user_follow):
        if user_sub is not user_follow:
            obj = self.filter(user_sub=user_sub, user_follow=user_follow)
            return True if obj.exists() else False
        else:
            return False


class Subscription(models.Model):
    user_sub = models.ForeignKey(to=User, related_name='user_sub', on_delete=models.CASCADE)
    user_follow = models.ForeignKey(to=User, related_name='user_follow', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    object = SubQuerySet.as_manager()

    def __str__(self):
        return f'{self.user_sub} подписан на {self.user_follow}'
