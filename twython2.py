# Twython.
# by Tatjana Scheffler
# A simple example script for corpus collection from Twitter using Tweepy https://github.com/tweepy

import tweepy
from tweepy import OAuthHandler


consumer_key = "HJ0pt8J1yTSKH8FBDTzIXbtiC"
consumer_secret = "X2VFcHsRInWOqEUgufP6rhOmnnzOmf1fCCQZC3yqQy3FH748JB"
access_token = "237815834-swF0v3WSt4q4rERCR1QbD1mmyv7hSTAh26kums9y"
access_secret = "b2unI0NdJrSRSq0J3aMuwAA5IR7HF7Tee8Cx7vpIYtsoD"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python1007.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('error')
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#refugeesNOTwelcome‏']) 
twitter_stream.filter(track=["refugees‏", "immigrants","islam","muslim","assimilate"])
