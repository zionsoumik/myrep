import tweepy
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import matplotlib.pyplot as plt
import codecs
#Variables that contains the user credentials to access Twitter API
atoken =
asecret =
ckey =
csecret =
f=open("new.txt","w")


import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com


# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        print(data)
        decoded = json.loads(data)
        print(decoded.keys())
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users)
        if "user" in decoded.keys():
            print ('@%s:%s' % (decoded['user']['screen_name'], decoded['text'].encode('latin1', 'ignore').decode('utf8', 'ignore')))
            print (decoded['user']['location'].encode('latin1','ignore').decode('utf8', 'ignore'))
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    print ("Showing all new tweets for #programming:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['the','python'],follow=["840372853"])