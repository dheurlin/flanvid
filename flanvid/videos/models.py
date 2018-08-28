from django.db import models
from .validators import validate_yt_url

class YouTubeURL(models.CharField):
    description = "A field for urls pointing to youtube videos"

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_yt_url]
        super().__init__(*args, **kwargs)


class Video(models.Model):
    url = YouTubeURL(max_length=200)
    # vid_id = models.IntegerField()
