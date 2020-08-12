import requests

#what shall I do?


headers = {
    'Client-ID': twitchID,
}

params = (
    ('id', 'AwkwardHelplessSalamanderSwiftRage'),
)

response = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)