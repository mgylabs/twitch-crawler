# Twitch Highlights

Finds twitch stream's highlights in previous VODs.

This program recieves twitch video URL as input, and finds highlight moments using clips and chats embedded in the stream.

This program uses OAuth client credential flow in order to retrieve access token for twitch API

# Executing process
1. Write certificate.py in src/crawler and add variable 'clientID' and 'clientSecret' for API requests

2. Run gettoken.py first in order to recieve access token. This will make accessToken.py by itself

3. Add chromedriver.exe under src/crawler (download it at https://chromedriver.chromium.org/)

4. Run crawler.py

# Requirements
This program requires a client ID and client secret in order to access twitch API

*This can be changed when further updates change the OAuth authorization flow*

# References
https://dev.twitch.tv/docs/api

https://dev.twitch.tv/docs/authentication

