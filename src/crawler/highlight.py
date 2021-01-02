from crawl import twitchCrawler
import datetime
from matplotlib import pyplot as plt

twitchCrawler = twitchCrawler()
clips = twitchCrawler.getClips()
chats = twitchCrawler.getChats()

#calculate highlight


#eliminate miliseconds create rfc class?
def rfcCut(rfc):
    rfc = rfc[:rfc.find('.')]
    return rfc

def rfcSubt(rfc, second):
    rfc = rfc[:-1]
    if int(rfc[-2:]) >= second:
        rfc = rfc[:-3] + ':' + str(int(rfc[-2:]) - second) + 'Z'
    else:
        rfc = rfc[:-6] + ':' + str(int(rfc[-5:-3])-1)+':'+ str(60-(second-int(rfc[-2:]))) +'Z'
    return rfc
#2020-10-25T10:13:34Z



#chat highlights

chatFrequency = dict()
i=0
while i+1 < len(chats):
    a=1
    while rfcCut(chats[i]["time"]) == rfcCut(chats[i+1]["time"]):
        a+=1
        i+=1
    chatFrequency[rfcCut(chats[i]["time"])] = a
    i+=1

highlightWeight = chatFrequency

#highlight weight: clips
for clip in clips:
    highlightWeight[clip['created_at']]


#graph



#highlights


#highligt weight: chat amount
#highlight weight: chat amount compared