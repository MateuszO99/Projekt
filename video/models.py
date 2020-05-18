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
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    to_watch = models.ManyToManyField(User, related_name='to_watch', blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

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
