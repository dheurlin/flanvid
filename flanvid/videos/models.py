from django.db import models
from .validators import validate_yt_id
from .youtube import get_vid_metadata

import json

class YouTubeID(models.CharField):
    description = "A field for youtube video ids"

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [validate_yt_id]
        super().__init__(*args, **kwargs)


class Video(models.Model):
    vid_id = YouTubeID(max_length=200, unique=True)
    title = models.CharField(max_length=500)
    thumb_url = models.CharField(max_length=500)
    curr_playing = models.BooleanField(default=False)

    points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        title, thumb = get_vid_metadata(self.vid_id)
        self.title = title
        self.thumb_url = thumb

        # If no other videos are submitted, set this one to be currently playing
        if Video.objects.count() == 0:
            self.curr_playing = True

        super().save(*args, **kwargs)  # Call the "real" save() method.


VOTE_UP   = "up"
VOTE_DOWN = "down"

def vote_to_point(vote_type):
    if vote_type == VOTE_UP:   return  1
    if vote_type == VOTE_DOWN: return -1
    else:                      return  0

class VidVotes:
    """A class representing the set of videos the user has voted for"""
    def __init__(self, json_data=None):
        if json_data == None:
            self.vids = {}
        else:
            self.vids = json.loads(json_data)

    def to_json(self):
        return json.dumps(self.vids)

    def add_vote(self, vid_id, vote_type):
        if vid_id in  self.vids:
            raise ValueError("Already voted!")
        else:
            self.vids[vid_id] = vote_type

    def change_vote(self, vid_id, vote_type):
        self.vids[vid_id] = vote_type

    def remove_vote(self, vid_id):
        del self.vids[vid_id]

    def has_voted_for(self, vid_id):
        return vid_id in self.vids

    def get_vote_for(self, vid_id):
        return self.vids[vid_id]

