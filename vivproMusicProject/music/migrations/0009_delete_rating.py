# Generated by Django 4.2.2 on 2024-07-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
