# Generated by Django 4.2.2 on 2024-07-17 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_song_star_rating_song_rating_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='music.song')),
            ],
        ),
    ]
