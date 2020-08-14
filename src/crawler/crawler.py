import requests
from certificate import twitchClientID, clientSecret
from videoinput import videoID
from accessToken import token

accessToken = token["access_token"]

def getVideo():
    headers = {
        'Client-ID': twitchClientID,
        'Authorization': 'Bearer '+accessToken
    }
    params = {
        'id': '709618396'
    }

    videoresponse = requests.get('https://api.twitch.tv/helix/videos', headers=headers, params=params)
    return videoresponse.text

def getClip() :
    headers = {
        'Client-ID': twitchClientID,
        'Authorization': 'Bearer '+accessToken
    }

    params = {
        'broadcaster_id': 'ffff'#,
        #'after': '',
        #'before' : '',
        #'first': ''
    }

    response = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)

print(getVideo())

