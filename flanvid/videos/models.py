from django.db import models

class Video(models.Model):
    url = models.CharField(max_length=200)
    # vid_id = models.IntegerField()
