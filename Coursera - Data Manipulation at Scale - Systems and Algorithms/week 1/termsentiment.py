"""
Solution for Problem 3: Derive the sentiment of new terms

Calculates sentiment score for words that don't have an intrinsic sentiment value. For example, if the word soccer
always appears in proximity with positive words like great and fun, then we can deduce that the term soccer itself
carries a positive sentiment. Terms and their scores are printed in order - from highest to lowest.

This script takes two arguments - a file containing pre-computed sentiment scores and another file containing
pre-exported tweet information in json format.
"""

import json
import re
import sys


class TermAnalyzer:

    def __init__(self):

        self.sentiment_score_file = sys.argv[1]
        self.twitter_data_file = sys.argv[2]

        self.sentiment_lookup = {}
        self.create_sentiment_lookup()

        self.terms = {}
        self.calculate_term_scores()

        self.sort_by_ratio()

        for term in self.terms:
            print(term[0], term[1]['avg_score'])

    def calculate_term_scores(self):

        with open(self.twitter_data_file, 'r') as f:
            for line in enumerate(f.readlines()):

                tweet = json.loads(line)['text']
                words_in_tweet = [word.strip('\'').lower() for word in re.split('[^0-9A-Za-z\']+', str(tweet))
                                  if word.strip('\'')]

                sentiment_score = 0
                for word in words_in_tweet:
                    if word in self.sentiment_lookup:
                        sentiment_score += self.sentiment_lookup[word]

                for word in words_in_tweet:
                    if word in self.sentiment_lookup:
                        pass
                    elif word not in self.terms:
                        self.terms[word] = {}
                        self.terms[word]['count'] = 1
                        self.terms[word]['tot_score'] = float(sentiment_score)
                        self.terms[word]['avg_score'] = float(sentiment_score)
                    else:
                        self.terms[word]['count'] += 1
                        self.terms[word]['tot_score'] += sentiment_score
                        self.terms[word]['avg_score'] = self.terms[word]['tot_score'] / self.terms[word]['count']

    def create_sentiment_lookup(self):

        with open(self.sentiment_score_file, 'r') as f:
            for line in f.readlines():
                self.sentiment_lookup[line.split('\t')[0].strip()] = int(line.split('\t')[1])

    def sort_by_ratio(self):

        sorted_terms = sorted(self.terms.items(), key=lambda x: x[1]['avg_score'], reverse=True)

        self.terms = sorted_terms


if __name__ == '__main__':
    TermAnalyzer()
