# Generated by Django 2.1 on 2018-08-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_remove_video_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
