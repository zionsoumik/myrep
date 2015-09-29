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
class Listener(StreamListener):

    def on_data(self, data):
        print (data)
        return True
    def on_error(self, status):
        print (status)

api = tweepy.API(auth)
listener = Listener()
stream = Stream(auth, listener)
myfeed_tweets = stream.userstream()
for item in myfeed_tweets:
    print (item)
    pprint(dir(item)) # trying to print attributes of item