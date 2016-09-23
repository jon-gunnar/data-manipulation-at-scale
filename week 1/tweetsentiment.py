"""
Solution for Problem 2: Derive the sentiment of each tweet

Calculates sentiment score for each tweet. The scores are printed in order of appearance.

This script takes two arguments - a file containing pre-computed sentiment scores and another file containing
pre-exported tweet information in json format.
"""

import sys
import json
import re


class SentimentAnalyzer:

    def __init__(self):

        self.sentiment_score_file = sys.argv[1]
        self.twitter_data_file = sys.argv[2]

        self.sentiment_lookup = {}
        self.create_sentiment_lookup()

        self.calculate_tweet_sentiment()

    def create_sentiment_lookup(self):

        with open(self.sentiment_score_file, 'r') as f:
            for line in f.readlines():
                self.sentiment_lookup[line.split('\t')[0].strip()] = int(line.split('\t')[1])

    def calculate_tweet_sentiment(self):

        with open(self.twitter_data_file, 'r') as f:
            for line in f.readlines():
                tweet_text = json.loads(line)['text']
                words_in_tweet = [word.strip('\'').lower() for word in re.split('[^0-9A-Za-z\']+', str(tweet_text))
                                  if word.strip('\'')]

                tweet_sentiment = 0
                for word in words_in_tweet:
                    if word in self.sentiment_lookup:
                        tweet_sentiment += self.sentiment_lookup[word]

                print(tweet_sentiment)


if __name__ == '__main__':
    SentimentAnalyzer()
