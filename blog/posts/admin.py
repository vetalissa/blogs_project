from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_name', 'date_create', 'user')
    fields = ('title_name', 'description', 'date_create', 'user')
    readonly_fields = ('date_create', 'user')


class PostLineAdmin(admin.TabularInline):
    model = Post
    fields = ('title_name', 'date_create')
    readonly_fields = ('title_name', 'description', 'date_create', 'user')
    extra = 0
