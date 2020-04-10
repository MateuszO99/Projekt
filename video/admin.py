from django.contrib import admin
from .models import Video, Comment


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'username', 'created')
    search_fields = ('video', 'username', 'created')


admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
