from django.forms import ValidationError

from .youtube import is_valid_id, url_to_id

def validate_yt_id(value):
    """ Check that the url points to a valid youtube video """
    if not is_valid_id(value):
        raise ValidationError("Not a valid YouTube vide id")

def validate_yt_url(value):
    """ Check that the url points to a valid youtube video """
    try:
        youtube_id = url_to_id(value)
    except Exception as e:
        print("=============================")
        print(str(e))
        print("=============================")
        raise ValidationError("Invalid Youtube URL")

    validate_yt_id(youtube_id)
