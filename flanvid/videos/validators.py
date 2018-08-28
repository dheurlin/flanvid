from django.forms import ValidationError

import re

def validate_yt_url(value):
    """ Check that the url points to a valid youtube video """
    if not re.match(r"youtube", value):
        raise ValidationError("Not a valid YouTube URL")
