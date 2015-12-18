import json

import tweepy
import requests

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# res = requests.get('http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp')
# data = res.text[15:-1]
# json_data = json.loads(data)
# games = json_data['games']

# =====================================================================
# Testing shit
# =====================================================================
with open('ot_SJS.json', 'r') as data_file:
    data = data_file.read()
    games = json.loads(data)


def parse_game(game):

    game_prog = game['tsc']
    game_status = game['bs']
    game_period = game['ts']
    away_team_name = game['atn']
    away_team_score = game['ats']
    home_team_name = game['htn']
    home_team_score = game['hts']

    if home_team_name == 'MontrĂŠal':
        home_team_name = 'Montreal'

    elif away_team_name == 'MontrĂŠal':
        away_team_name = 'Montreal'


    if game['tsc'] == 'progress' and \
        game['bs'] == 'LIVE' and \
        game['ts'] == 'END 3rd':
        pass
        # tweet_game(api, away_team_name, away_team_score,
        #             home_team_name, home_team_score)

    elif game['tsc'] == 'progress' and \
        game['bs'] == 'LIVE' and \
        game['ts'].split(" ")[1] == 'OT':

        print(away_team_name)
        # tweet_game(api, away_team_name, away_team_score,
        #             home_team_name, home_team_score)

def tweet_game(api, away_team_name, away_team_score,
                home_team_name, home_team_score):

    if home_team_score and away_team_score:
        score = home_team_score.text.lstrip().strip(" ")
    # if overtime:
    status = 'Tied at ' + score + away_team_name + ' @ ' + \
                home_team_name + ' in #3on3OT'
    print(status)
    # api.update_status(status=status)

for game in games:
    parse_game(game)
