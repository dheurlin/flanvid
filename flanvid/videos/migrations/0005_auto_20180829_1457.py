# Generated by Django 2.1 on 2018-08-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20180829_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='url',
            new_name='vid_id',
        ),
    ]