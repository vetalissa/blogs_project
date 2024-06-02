from django.contrib import admin

from comments.models import Commment


class CommentLineAdmin(admin.TabularInline):
    model = Commment
    fields = ('user', 'date_create', 'comment_text')
    readonly_fields = ('user', 'date_create', 'comment_text')
    extra = 0
