from django.contrib import admin

from likes.models import Like, UserLike


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'count_like')
    fields = ('post', 'count_like')


@admin.register(UserLike)
class UserLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    fields = ('post', 'user')


class LikePostLineAdmin(admin.TabularInline):
    model = Like
    fields = ('count_like',)
    extra = 0
