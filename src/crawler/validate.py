import requests
from accessToken import token

accessToken = token['access_token']

#validate
def validateToken():
    headers = {
        'Authorization': 'OAuth '+accessToken,
    }

    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)
    return response.text