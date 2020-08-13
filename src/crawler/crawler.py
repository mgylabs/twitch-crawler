import requests
from certificate import twitchClientID
#what shall I do?


def getVideo():
    headers = {
        'Client-ID': twitchClientID
    }
    params = {
        'id': '707902562'
    }

    videoresponse = requests.get('https://api.twitch.tv/helix/videos', headers=headers, params=params)
    return videoresponse.text

def getClip() :
    headers = {
        'Client-ID': twitchClientID
    }

    params = {
        'broadcaster_id': 'ffff'#,
        #'after': '',
        #'before' : '',
        #'first': ''
    }

    response = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)

print(getVideo())

