import crawl
import datetime

chats = crawl.chats

#calculate highlight
clip_weight = 0
chat_weight = 0
highlight_weight = 0

#convert RFC3339 into duration(seconds)
def rfcCut(rfc):
    rfc = rfc[:rfc.find('.')]
    return rfc

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

print(chatFrequency)

#graph



#highlights

#highligt weight: chat amount
#highlight weight: chat amount compared
#highlight weight: clips

