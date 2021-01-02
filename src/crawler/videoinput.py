broadcastURL = input('다시보기 주소:')
if '?' in broadcastURL:
    broadcastURL = broadcastURL.split('?')
    broadcastURL = broadcastURL[0]

if 'https://www.twitch.tv/videos/' in broadcastURL:
    videoID = broadcastURL[29:]
else:
    videoID = broadcastURL[21:]

