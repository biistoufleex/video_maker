import requests
import os
from dotenv import load_dotenv

load_dotenv()

'''
    Funtion de connection a l'api twitch
    Return le Token
'''


def get_token():
    # API CREDENTIALS
    CLIENT_ID = str(os.getenv('CLIENT_ID'))
    CLIENT_SECRET = str(os.getenv('CLIENT_SECRET'))

    # REQUEST PARAMS
    PARAMS = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': ''
    }

    # GET TOKEN URL
    URL = 'https://id.twitch.tv/oauth2/token'
    # sending get request and saving the response as response object
    r = requests.post(url=URL, data=PARAMS)

    # extracting data in json format
    data = r.json()

    return data
