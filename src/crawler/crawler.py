import requests
import json
from certificate import twitchClientID, clientSecret
from videoinput import videoID
from accessToken import token
from validate import validateToken

accessToken = token["access_token"]
#validate token
validateToken()

#get video
vidHeaders = {
    'Client-ID': twitchClientID,
    'Authorization': 'Bearer '+accessToken
}
vidParams = {
    'id': '709618396'
}

videoresponse = requests.get('https://api.twitch.tv/helix/videos', headers=vidHeaders, params=vidParams)
videoresponse = json.loads(videoresponse.text)
broadID = videoresponse['data'][0]['user_id']


#get clips
clipHeaders = {
    'Client-ID': twitchClientID,
    'Authorization': 'Bearer '+accessToken
}

clipParams = {
    'broadcaster_id': broadID
    #'after': '',
    #'before' : '',
    #'first': ''
}

response = requests.get('https://api.twitch.tv/helix/clips', headers=clipHeaders, params=clipParams)