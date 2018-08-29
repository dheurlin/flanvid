from django.db import models
from .validators import validate_yt_id

class YouTubeID(models.CharField):
    description = "A field for youtube video ids"

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_yt_id]
        super().__init__(*args, **kwargs)


class Video(models.Model):
    vid_id = YouTubeID(max_length=200, unique=True)
