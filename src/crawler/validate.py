import requests
from certificate import twitchClientID

#get token
params = {
    'client_id': twitchClientID,
    'redirect_uri': 'http://localhost',
    'response_type': 'token',
    'scope': 'clips:edit' #may be added further later for analytics
}

token = requests.get('https://id.twitch.tv/oauth2/authorize', params=params)
f = open("apirequest.html", 'w')
f.write(token.text)
f.close

#send token in api request

#validate