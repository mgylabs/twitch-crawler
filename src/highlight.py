#import matplotlib
#from crawler import crawl
import datetime

#calculate highlight
clip_weight = 0
chat_weight = 0
highlight_weight = 0

#convert RFC3339 into duration(seconds)
rfc2 = '2002-10-02T15:00:00.05Z'
rfc1 = '2002-10-02T13:03:09.05Z'
def rfctoList(rfc):
    rfc = rfc[:-rfc.find('.')].replace('-', ':').replace('T', ':').split(':')
    for r in range(len(rfc)):
        rfc[r] = int(rfc[r])
    return rfc

def subtRfc(rfc1, rfc2):
    rfc1= rfctoList(rfc1)
    rfc2= rfctoList(rfc2)
    rfc1= datetime.datetime(rfc1[0], rfc1[1], rfc1[2], rfc1[3], rfc1[4], rfc1[5])
    rfc2= datetime.datetime(rfc2[0], rfc2[1], rfc2[2], rfc2[3], rfc2[4], rfc2[5])
    result = rfc2-rfc1
    return result

vid_start = crawl.chats[0]['time']

for chat in chats:
    chat['time']=subtRfc(vid_start, chat['time'])

    

#graph

#highlights