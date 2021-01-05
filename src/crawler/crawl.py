import requests
import json
import datetime
import tempfile
import twitch
import itertools
import time
import pandas
from selenium import webdriver
from certificate import twitchClientID, clientSecret
from videoinput import videoID
from accessToken import token
from validate import validateToken

class twitchCrawler():
    def __init__(self):
        self.accessToken = token["access_token"]
        #validate token
        validateToken()

    def timeConvert(self, time):
        conv = time.replace('h', ':')
        conv = conv.replace('m', ':')
        conv = conv.replace('s', '')
        conv = conv.split(':')
        hour, minute = 0, 0
        if 'h' in time:
            hour = conv[0]
            if 'm' in time:
                minute = conv[1]
        elif 'm' in time: 
            minute = conv[0]
        conv = datetime.time(int(hour), int(minute)+1)
        time = '{0.hour:02}:{0.minute:02}'.format(conv)
        return time

    def getVideo(self):
        vidHeaders = {
            'Client-ID': twitchClientID,
            'Authorization': 'Bearer '+self.accessToken
        }
        vidParams = {
            'id': videoID
        }

        videoresponse = requests.get('https://api.twitch.tv/helix/videos', headers=vidHeaders, params=vidParams)
        videoresponse = json.loads(videoresponse.text)
        broadID = videoresponse['data'][0]['user_id']

        duration = videoresponse['data'][0]['duration']

        vidStarted = videoresponse['data'][0]['created_at'][:-1]+'+'+self.timeConvert(duration) #using RFC3339, 2019-10-12T07:20:50.52+01:00 = 2019-10-12T13:20:50.52Z
        vidEnded = videoresponse['data'][0]['created_at'] #RFC 3339

        return broadID, duration, vidStarted, vidEnded

    def getClips(self):
        broadID, duration, vidStarted, vidEnded = self.getVideo()

        clipHeaders = {
            'Client-ID': twitchClientID,
            'Authorization': 'Bearer '+self.accessToken
        }

        clipParams = {
            'broadcaster_id': broadID,
            'first': '100',
            'started_at': vidStarted,
        }
        options = webdriver.ChromeOptions()#to be edited
        options.add_argument("headless")#to be edited

        clipResponse = requests.get('https://api.twitch.tv/helix/clips', headers=clipHeaders, params=clipParams)
        clipResponse = json.loads(clipResponse.text)['data']
        '''
        driver = webdriver.Chrome(executable_path='src\crawler\chromedriver.exe', chrome_options=options)
        driver.get(url=clipURL)
        href = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div/main/div/div/div[2]/div[2]/div[3]/div/div/div/a')
        starts_at = href.get_attribute('href')
        '''

        clips = []
        for a in range(len(clipResponse)):
            if clipResponse[a]['video_id'] == videoID:
                clips.append(clipResponse[a])

        return clips

    def getChats(self):
        start = time.time()
        helix_api = twitch.Helix(client_id=twitchClientID, bearer_token=self.accessToken, use_cache=True)
        chats = {'created_at': [], 'name': [], 'message': []}
        #chat dictionary nested inside 'chats' list
        for comment in helix_api.video(videoID).comments:
            #chats.append(dict(time=comment.created_at, name=comment.commenter.display_name, message=comment.message.body))
            chats['created_at'].append(comment.created_at)
            chats['name'].append(comment.commenter.display_name)
            chats['message'].append(comment.message.body)
        print(time.time()-start)
        df = pandas.DataFrame(chats)
        df.to_csv('src/crawler/chatfiles/chats.csv', header=False, index=False) 
        return df

crawl = twitchCrawler()
print(crawl.getChats().head())

