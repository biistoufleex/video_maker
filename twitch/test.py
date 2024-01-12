from dotenv import load_dotenv
import os
import requests
from twitch_token import get_token
from download_clip import download_clip

load_dotenv()

CLIENT_ID = str(os.getenv('CLIENT_ID'))
OAUTH_TOKEN = get_token()

URL = 'https://api.twitch.tv/helix/clips?{PARAMS}'
HEADER = {
    'Client-id': CLIENT_ID,
    'Authorization': "Bearer " + OAUTH_TOKEN['access_token']
}

PARAMS = {
    'broadcaster_id': '26301881',
    'first': '1'
}

r = requests.get(url=URL, headers=HEADER, params=PARAMS)
data = r.json()

video_data = data['data'][0]
video_link = video_data['thumbnail_url'].replace("-preview-480x272.jpg", ".mp4")

download_clip(video_link, video_data['title'])
