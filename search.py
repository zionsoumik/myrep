__author__ = 'Soumik'
import tweepy
atoken =
asecret =
ckey =
csecret =
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.search(q="sljs")
print(type(public_tweets))
for tweet in public_tweets:
    print(type(tweet))
    print(tweet.text.encode("ascii",errors="replace").decode("utf8"))