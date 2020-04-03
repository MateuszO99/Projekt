from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to='video_list')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('video:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Komentarz dodany przez {self.username} dla filmu {self.video}'

    class Meta:
        ordering = ('created',)
