import tweepy

from bot.messages import messages
from bot.teams import teams
from bot.utils import fetch_games


def get_games():
    games = fetch_games()
    return games


def game_is_ot(game):
    return


def get_message(stage):
    return


def tweet_game():
    return
