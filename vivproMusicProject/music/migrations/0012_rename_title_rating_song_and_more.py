# Generated by Django 4.2.2 on 2024-07-17 11:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0011_rename_song_rating_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='title',
            new_name='song',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'song')},
        ),
    ]