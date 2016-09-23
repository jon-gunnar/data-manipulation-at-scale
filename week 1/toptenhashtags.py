"""
Solution for Problem 6: Top ten hash tags

Calculates frequencies for all hash tags in the data set. Prints top ten hash tags and their frequencies in order
from most to least frequent.

This script takes one argument - a text file with one tweet per line in json format.
"""

import collections
import json
import sys


class HashTagAnalyzer:

    def __init__(self):

        self.twitter_data_file = sys.argv[1]

        self.hash_tag_counts = collections.defaultdict(int)
        self.count_hash_tags()
        self.total_hash_tag_count = sum(self.hash_tag_counts.values())

        self.hash_tag_frequencies = []
        self.calculate_hash_tag_frequencies()

        for hash_tag, frequency in self.hash_tag_frequencies:
            print(hash_tag, frequency)

    def calculate_hash_tag_frequencies(self):

        for hash_tag, count in self.hash_tag_counts.items():
            self.hash_tag_frequencies.append((hash_tag, float(count / self.total_hash_tag_count)))

        self.hash_tag_frequencies.sort(key=lambda x: x[1], reverse=True)

    def count_hash_tags(self):

        with open(self.twitter_data_file, 'r') as f:
            for line in f.readlines():

                tweet = json.loads(line)

                for hash_tag in tweet['entities']['hashtags']:
                    self.hash_tag_counts[hash_tag['text'].lower()] += 1


if __name__ == '__main__':
    HashTagAnalyzer()
