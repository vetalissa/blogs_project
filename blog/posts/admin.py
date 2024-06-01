from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_name', 'date_create', 'author')
    fields = ('title_name', 'description', 'date_create', 'author')
    readonly_fields = ('date_create', 'author')


class PostLineAdmin(admin.TabularInline):
    model = Post
    fields = ('title_name', 'date_create')
    readonly_fields = ('title_name', 'description', 'date_create', 'author')
    extra = 0
