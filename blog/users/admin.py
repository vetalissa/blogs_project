from django.contrib import admin
from users.models import User
from posts.admin import PostLineAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (PostLineAdmin, )
