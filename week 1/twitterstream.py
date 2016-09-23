"""
Solution to Problem 1: Get Twitter Data

This script filters Twitter stream for specified parameters and saves the results in json format.
"""

import tweepy
import json
import time

API_KEY = '<Consumer Key (API Key)>'
API_SECRET = '<Consumer Secret (API Secret)>'
ACCESS_TOKEN_KEY = '<Access Token>'
ACCESS_TOKEN_SECRET = '<Access Token Secret>'

# Authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.access_token = ACCESS_TOKEN_KEY
auth.access_token_secret = ACCESS_TOKEN_SECRET


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        with open('output.txt', 'a') as f:
            json.dump(status._json, f)
            f.write('\n')

    def on_error(self, status_code):

        time.sleep(120)


if __name__ == '__main__':

    my_stream_listener = MyStreamListener()
    my_stream = tweepy.Stream(auth=auth, listener=my_stream_listener)
    my_stream.filter(track=['data'], languages=['en'])
