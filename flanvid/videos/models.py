from django.db import models
from .validators import validate_yt_id
from .youtube import get_vid_metadata

class YouTubeID(models.CharField):
    description = "A field for youtube video ids"

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_yt_id]
        super().__init__(*args, **kwargs)


class Video(models.Model):
    vid_id = YouTubeID(max_length=200, unique=True)
    title = models.CharField(max_length=500)
    thumb_url = models.CharField(max_length=500)

    points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        title, thumb = get_vid_metadata(self.vid_id)
        self.title = title
        self.thumb_url = thumb

        super().save(*args, **kwargs)  # Call the "real" save() method.
