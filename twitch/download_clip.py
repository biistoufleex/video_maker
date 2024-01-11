from twitch_token import get_token
import requests
import os
from dotenv import load_dotenv

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

response = requests.get(video_link)

if response.status_code == 200:

    contenu_video = response.content
    with open("twitch/videos/" + video_data["id"] + ".mp4", "wb") as f:
        f.write(contenu_video)
    print("La vidéo a été téléchargée avec succès.")

else:
    print("La requête a échoué avec le code d'erreur :", response.status_code)
