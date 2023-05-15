from django.contrib import admin
from django.utils.html import format_html

from .models import Gallery, Picture


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'icon')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gallery', 'created_at', 'image_tag')
    list_filter = ('gallery',)
    search_fields = ('name', 'gallery__name')

    def image_tag(self, obj):
        return format_html('<img class="image" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
