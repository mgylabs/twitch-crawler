import requests
import json
from certificate import twitchClientID, clientSecret
from videoinput import videoID
from accessToken import token
from validate import validateToken
import datetime

accessToken = token["access_token"]
#validate token
validateToken()

def timeConvert(time):

    time = time.split('h') #4, 8m12s
    time[1] = time[1].split('m')[0]

    time = datetime.time(int(time[0]), int(time[1])+1) 
    time = '{0.hour:02}:{0.minute:02}'.format(time)

    return time

#get video
vidHeaders = {
    'Client-ID': twitchClientID,
    'Authorization': 'Bearer '+accessToken
}
vidParams = {
    'id': videoID
}

videoresponse = requests.get('https://api.twitch.tv/helix/videos', headers=vidHeaders, params=vidParams)
videoresponse = json.loads(videoresponse.text)
broadID = videoresponse['data'][0]['user_id']

duration = videoresponse['data'][0]['duration']


vidStarted = videoresponse['data'][0]['created_at'][:-1]+'+'+timeConvert(duration) #using RFC3339, 2019-10-12T07:20:50.52+01:00 = 2019-10-12T13:20:50.52Z
vidEnded = videoresponse['data'][0]['created_at'] #RFC 3339


#get clips
clipHeaders = {
    'Client-ID': twitchClientID,
    'Authorization': 'Bearer '+accessToken
}

clipParams = {
    'broadcaster_id': broadID,
    'first': '100',
    'started_at': vidStarted,
}

clipResponse = requests.get('https://api.twitch.tv/helix/clips', headers=clipHeaders, params=clipParams)
clipResponse = json.loads(clipResponse.text)['data']
clips = []
for a in range(len(clipResponse)):
    if clipResponse[a]['video_id'] == videoID:
        clips.append(clipResponse[a])
# list of clips created in the video given

#get chat


