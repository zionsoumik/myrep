__author__ = 'Soumik'
import tweepy
atoken =
asecret =
ckey =
csecret =
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(type(tweet))
    print(tweet.truncated)

    print(tweet.text.encode("ascii",errors="ignore").decode("utf-8"))
'''  Status {

 'contributors':
 'truncated':
 'text':
 'in_reply_to_status_id':
 'id':
 '_api':
 'author':
 'retweeted':
 'coordinates':
 'source':
 'in_reply_to_screen_name':
 'id_str':
 'retweet_count':
 'in_reply_to_user_id':
 'favorited':
 'retweeted_status':
 'source_url':
 'user':
 'geo':
 'in_reply_to_user_id_str':
 'created_at':
 'in_reply_to_status_id_str':
 'place':
}'''