# Generated by Django 2.1.7 on 2020-03-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='username',
        ),
    ]
