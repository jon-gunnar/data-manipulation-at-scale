"""
Solution for Problem 4: Compute Term Frequency

Computes the frequency of any one-word term among all terms within the given tweet file. Terms and their frequencies
are printed in order from most to least frequent.

This script takes one argument - a text file with one tweet per line in json format.
"""

import collections
import json
import re
import sys


class FrequencyCalculator:

    def __init__(self):

        self.twitter_data_file = sys.argv[1]

        self.tot_terms = 0
        self.term_counts = collections.defaultdict(int)
        self.count_term_occurrences()

        self.term_frequencies = []
        self.calculate_term_frequencies()

        self.sort_by_frequency()

        for term in self.term_frequencies:
            print(*term)

    def calculate_term_frequencies(self):

        for term, count in self.term_counts.items():
            self.term_frequencies.append((term, float(count / self.tot_terms)))

    def count_term_occurrences(self):

        with open(self.twitter_data_file, 'r') as f:
            for line in f.readlines():

                tweet = json.loads(line)['text']
                words_in_tweet = [word.strip('\'').lower() for word in re.split('[^0-9A-Za-z\']+', str(tweet))
                                  if word.strip('\'')]

                for word in words_in_tweet:
                    self.tot_terms += 1
                    self.term_counts[word] += 1

    def sort_by_frequency(self):

        sorted_frequencies = sorted(self.term_frequencies, key=lambda x: x[1], reverse=True)

        self.term_frequencies = sorted_frequencies


if __name__ == '__main__':
    FrequencyCalculator()
