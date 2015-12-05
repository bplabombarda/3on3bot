import tweepy
import requests
from bs4 import BeautifulSoup


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

res = requests.get('sportsnet.ca/hockey/nhl/scores/')
game_cards = BeautifulSoup(res.text, 'html.parser')


def tweet3on3(game_card, api):
    away_team = ""
    home_team = ""

    status = away_team + " @ " + home_team + " #3on3bot"
    api.update_status(status)


for card in game_cards:
    tweet3on3(card, api)
