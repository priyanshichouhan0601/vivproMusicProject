# Generated by Django 4.2.2 on 2024-07-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_song_num_songs_remove_song_speechiness'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='acoustic',
            new_name='acousticness',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='dance',
            new_name='danceability',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='duration',
            new_name='duration_ms',
        ),
        migrations.AddField(
            model_name='song',
            name='key',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='num_bars',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='time_signature',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]