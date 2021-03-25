from django.contrib import admin
from .models import PhotoMedia, VideoMedia


class MediaBankPhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(PhotoMedia, MediaBankPhotoAdmin)

class MediaBankVideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(VideoMedia, MediaBankPhotoAdmin)