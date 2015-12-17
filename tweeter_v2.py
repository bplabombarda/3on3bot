import json

import tweepy
import requests
from bs4 import BeautifulSoup

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

res = requests.get('http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp')
data = res.text[15:-1]
json_data = json.loads(data)
games = json_data['games']

for game in games:
    if game['bs'] == "FINAL OT":
