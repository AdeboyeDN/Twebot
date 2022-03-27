import tweepy
from time import sleep
from keys import *
from action import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




user = api.get_user(screen_name='twitter')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

