__author__ = 'Soumik'
import tweepy
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import matplotlib.pyplot as plt
import codecs
atoken =
asecret =
ckey =
csecret =
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
twitterApi = tweepy.API(auth)
f=open("new.txt",'w')
def iterjsoon(f):
    for key in f.keys():
        if(isinstance(f[key],dict)):
            uprint(key,":")
            print("{")
            iterjsoon(f[key])
            print("}")
        else:
            uprint(key,":",f[key])
class ReplyToTweet(StreamListener):
    def on_data(self, data):
        s=json.loads(data)

        print("hello")
        iterjsoon(s)


    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = ReplyToTweet()
    twitterStream = Stream(auth, l)
    twitterStream.filter(track=['car','bike'],follow=['840372853'])