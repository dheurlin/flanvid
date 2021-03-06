import requests
import json
import re

API_KEY = 'AIzaSyAnqbHR1Ypww6jpFPEsT3QgdbPqQj2fKd0'

def is_valid_id(yt_id):
    """Checks if the given string is a valid youtube video id"""
    r = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=id&id={yt_id}&key={API_KEY}")
    try:
        return r.json()['pageInfo']['totalResults'] != 0
    except:
        return False

def get_vid_metadata(yt_id):
    """Gets the video title and thumbnail url, and return them as a tuple"""

    r = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={yt_id}&key={API_KEY}")

    snippet = r.json()['items'][0]['snippet']
    return (snippet['title'], snippet['thumbnails']['default']['url'])

def url_to_id(yt_url):
    """Converts a youtube URL to a Video ID"""
    try:
        match = re.search('\.[a-zA-Z]*\/(watch\?v=)?(.+)', yt_url)
        return match.group(match.lastindex)

    except:
       raise ValueError("Invalid youtube url!")
