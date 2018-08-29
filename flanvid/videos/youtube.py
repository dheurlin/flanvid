import requests
import json

API_KEY = 'AIzaSyAnqbHR1Ypww6jpFPEsT3QgdbPqQj2fKd0'

def is_valid_id(yt_id):
    """Checks if the given string is a valid youtube video id"""
    r = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=id&id={yt_id}&key={API_KEY}")
    try:
        return r.json()['pageInfo']['totalResults'] != 0
    except:
        return False

