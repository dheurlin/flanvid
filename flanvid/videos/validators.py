from django.forms import ValidationError

from .youtube import is_valid_id

def validate_yt_id(value):
    """ Check that the url points to a valid youtube video """
    if not is_valid_id(value):
        raise ValidationError("Not a valid YouTube vide id")
