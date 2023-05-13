from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff', 'avatar_tag']
    list_filter = ['is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img class="avatar" src="{}" />'.format(obj.avatar.url))

    avatar_tag.short_description = 'Avatar'
