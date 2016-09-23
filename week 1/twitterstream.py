"""
Solution to Problem 1: Get Twitter Data

This script filters Twitter stream for specified parameters and saves the results in json format.
"""

import tweepy
import json
import time

API_KEY = 'kCJRInYQhmRxxd0BkqLJElU1u'
API_SECRET = 'jd3Bd8uV95INSGRbiyYngNmY36Vf9HEucWA6yVVkIQupXlj0pg'
ACCESS_TOKEN_KEY = '776780584341409792-2MmhTDhjfNy7Y8B1qVLcTJckIFZXS13'
ACCESS_TOKEN_SECRET = 'RTk2jiXYeFAeq3P5cjJNJvS7Fr1RHDqO05QtlvoJVaj2W'

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
