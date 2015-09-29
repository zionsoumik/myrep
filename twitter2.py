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
class listener(StreamListener):

    def on_data(self, data):
        print (data)
        return True
    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = listener()
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    print ("Showing all new tweets for #programming:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.userstream(_with="user")