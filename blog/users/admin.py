from django.contrib import admin

from posts.admin import PostLineAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (PostLineAdmin, )
