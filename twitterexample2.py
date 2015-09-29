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
# Redirect user to Twitter to authorize
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# Get access token


# Construct the API instance
api = tweepy.API(auth)
# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    print(friend.screen_name)
    user = api.get_user(str(friend.screen_name))
    for f2 in user.friends():
        for status in tweepy.Cursor(api.user_timeline, id=user.id).items():
    # process status here
            print(status.text.encode('ascii',errors='ignore').decode('utf-8'))
        print(f2.screen_name)

# Iterate through the first 200 statuses in the friends timeline
'''
user object
{
 'follow_request_sent': False,
 'profile_use_background_image': True,
 'id': 132728535,
 '_api': <tweepy.api.api object="" at="" xxxxxxx="">,
 'verified': False,
 'profile_sidebar_fill_color': 'C0DFEC',
 'profile_text_color': '333333',
 'followers_count': 80,
 'protected': False,
 'location': 'Seoul Korea',
 'profile_background_color': '022330',
 'id_str': '132728535',
 'utc_offset': 32400,
 'statuses_count': 742,
 'description': "Cars, Musics, Games, Electronics, toys, food, etc... I'm just a typical boy!",
 'friends_count': 133,
 'profile_link_color': '0084B4',
 'profile_image_url': 'http://a1.twimg.com/profile_images/1213351752/_2_2__normal.jpg',
 'notifications': False,
 'show_all_inline_media': False,
 'geo_enabled': True,
 'profile_background_image_url': 'http://a2.twimg.com/a/1294785484/images/themes/theme15/bg.png',
 'screen_name': 'jaeeeee',
 'lang': 'en',
 'following': True,
 'profile_background_tile': False,
 'favourites_count': 2,
 'name': 'Jae Jung Chung',
 'url': 'http://www.carbonize.co.kr',
 'created_at': datetime.datetime(2010, 4, 14, 1, 20, 45),
 'contributors_enabled': False,
 'time_zone': 'Seoul',
 'profile_sidebar_border_color': 'a8c7f7',
 'is_translator': False,
 'listed_count': 2
}
'''