from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'description')


admin.site.register(Video, VideoAdmin)
