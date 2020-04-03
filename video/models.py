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
