import os
import json
import logging

import tweepy
import requests

dir_path = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename='error.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# =====================================================================
# Testing Credentials
# =====================================================================
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

url = 'http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
                            AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/47.0.2526.106 Safari/537.36'}
res = requests.get(url, headers=headers)
data = res.text[15:-1]
json_data = json.loads(data)
games = json_data['games']

# =====================================================================
# Testing shit
# =====================================================================
# with open(os.path.join(dir_path, 'ot_SJS.json'), 'r') as data_file:
#     data = data_file.read()
#     games = json.loads(data)

# =====================================================================
# Load hashtag JSON file
# =====================================================================
with open(os.path.join(dir_path, 'hashtags.json'), 'r') as ht_file:
    data = ht_file.read()
    hashtags = json.loads(data)


def parse_game(game, hashtags):

    game_prog = game['tsc']
    game_status = game['bs']
    game_period = game['ts']
    away_team_name = game['atv']
    away_team_score = game['ats']
    home_team_name = game['htv']
    home_team_score = game['hts']

    # =====================================================================
    # Find team hashtags
    # =====================================================================
    for hashtag in hashtags:
        if hashtag['team_name'] == away_team_name:
            away_team_ht = hashtag['hashtag']

        if hashtag['team_name'] == home_team_name:
            home_team_ht = hashtag['hashtag']

    # =====================================================================
    # Check END 3RD
    # =====================================================================
    if game['bs'] == 'LIVE' and \
        game['ts'] == 'END 3rd':

        tweet_game(api, away_team_ht, away_team_score,
                    home_team_ht, home_team_score)

    # =====================================================================
    # Check OT
    # =====================================================================
    elif game['bs'] == 'LIVE' and \
        game['ts'].split(" ")[1] == 'OT':

        tweet_game(api, away_team_ht, away_team_score,
                    home_team_ht, home_team_score)


def tweet_game(api, away_team_ht, away_team_score,
                home_team_ht, home_team_score):

    if home_team_score == away_team_score:
        score = home_team_score
        status = away_team_ht + ' @ ' + home_team_ht + \
                    ' tied at ' + score + ' in #3on3OT'
        # print(status)
        api.update_status(status=status)

    else:
        pass

for game in games:
    parse_game(game, hashtags)
