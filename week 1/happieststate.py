"""
Solution for Problem 5: Which State is happiest?

Finds the US state with most positive tweets. Prints abbreviated name of the "happiest" state and its average
tweet sentiment score.

This script takes two arguments - a file containing pre-computed sentiment scores and another file containing
pre-exported tweet information in json format.
"""


import sys
import json
import re

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def get_state(*locations):

    locations = [location for location in locations if location]

    if not locations:
        return False

    for location in locations:

        for abbreviation, state in STATES.items():
            if state in location:
                return abbreviation

        for abbreviation in STATES:
            if abbreviation == location.split(' ')[-1].strip():
                return abbreviation

        return False


class StateAnalyzer:

    def __init__(self):

        self.sentiment_score_file = sys.argv[1]
        self.twitter_data_file = sys.argv[2]

        self.sentiment_lookup = {}
        self.create_sentiment_lookup()

        # [{text: '', state: '', score: ''}, ...]
        self.tweets = []
        self.create_tweet_list()

        # {state: [tot_score, tweet_cnt], ...}
        self.state_totals = {}
        self.create_state_list()

        self.state_ratios = []
        self.calculate_ratios()

        print(*self.state_ratios[0])

    def calculate_ratios(self):

        for state, values in self.state_totals.items():
            self.state_ratios.append((state, float(values[0] / values[1])))

        self.state_ratios.sort(key=lambda x: x[1], reverse=True)

    def calculate_tweet_sentiment(self, tweet_text):

        words_in_tweet = [word.strip('\'').lower() for word in re.split('[^0-9A-Za-z\']+', str(tweet_text))
                          if word.strip('\'')]

        tweet_sentiment = 0
        for word in words_in_tweet:
            if word in self.sentiment_lookup:
                tweet_sentiment += self.sentiment_lookup[word]

        return tweet_sentiment

    def create_sentiment_lookup(self):

        with open(self.sentiment_score_file, 'r') as f:
            for line in f.readlines():
                self.sentiment_lookup[line.split('\t')[0].strip()] = int(line.split('\t')[1])

    def create_state_list(self):

        for tweet in self.tweets:

            if tweet['state'] not in self.state_totals:
                self.state_totals[tweet['state']] = [tweet['score'], 1]
            else:
                self.state_totals[tweet['state']][0] += tweet['score']
                self.state_totals[tweet['state']][1] += 1

    def create_tweet_list(self):

        with open(self.twitter_data_file, 'r') as f:
            # todo remove enumerate
            for line in f.readlines():

                tweet = json.loads(line)

                state = get_state(tweet['user']['location'], tweet['user']['time_zone'])
                if state:
                    self.tweets.append({
                        'text': tweet['text'],
                        'state': state,
                        'score': self.calculate_tweet_sentiment(tweet['text'])
                    })


if __name__ == '__main__':
    StateAnalyzer()
