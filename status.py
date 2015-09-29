from tweepy import OAuthHandler
import tweepy
consumer_key =
consumer_secret =
access_token =
access_secret =
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#GITwo things can be done  
#1 : We can get n number of statuses from you time line 
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
    print(status.id)

#2 : We can get a particular status in a status object 
#This helps us tackle one particular tweet in different ways 648284922730315776
#author_details_keys = get_status(648284922730315776).author()._json.keys()
#author_details_values =