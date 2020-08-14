import requests
import time
from certificate import twitchClientID, clientSecret

#get token
def getToken():
    params = {
        'client_id': twitchClientID,
        #'redirect_uri': 'http://localhost',
        #'response_type': 'token',
        'client_secret': clientSecret,
        'grant_type': 'client_credentials',
        'scope': 'clips:edit' #may be added further later for analytics
    }

    token = requests.post('https://id.twitch.tv/oauth2/token', params=params)
    #accessToken = token['access_token']
    return token.text


#refreshing process needed


#validate
def validateToken():
    headers = {
        'Authorization': 'OAuth '+accessToken,
    }

    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)

f = open('./src/crawler/accessToken.py', 'w')
f.write('token =' +getToken())