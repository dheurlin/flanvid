# Generated by Django 2.1 on 2018-08-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_video_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='curr_playing',
            field=models.BooleanField(default=False),
        ),
    ]