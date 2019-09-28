import tweepy

from bot.config import config


CONSUMER_KEY = config["twitter_consumer_key"]
CONSUMER_SECRET = config["twitter_consumer_secret"]
ACCESS_TOKEN = config["twitter_access_token"]
ACCESS_TOKEN_SECRET = config["twitter_access_token_secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
