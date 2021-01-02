import requests
import time
from certificate import twitchClientID, clientSecret

#get token
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
token = token.text

f = open('./src/crawler/accessToken.py', 'w')
f.write('token =' + token)
