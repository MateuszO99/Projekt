# Generated by Django 2.1.7 on 2020-04-28 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0005_video_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='to_watch',
            field=models.ManyToManyField(blank=True, related_name='to_watch', to=settings.AUTH_USER_MODEL),
        ),
    ]
