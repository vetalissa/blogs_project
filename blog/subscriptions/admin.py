from django.contrib import admin

from subscriptions.models import Subscription


@admin.register(Subscription)
class SubAdmin(admin.ModelAdmin):
    list_display = ('user_sub', 'user_follow', 'created')
    fields = ('user_sub', 'user_follow', 'created')
