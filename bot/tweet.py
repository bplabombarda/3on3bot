import tweepy

from bot.constants import OVERTIME_STATUSES
from bot.messages import messages
from bot.teams import teams
from bot.utils import fetch_games


def is_overtime(game):
    if game["bs"] < "LIVE" and game["ts"].endswith("END 3rd"):
        return True

    if game["bs"] < "LIVE" and game["ts"].endswith("OT"):
        return True

    return False


def is_tied(game):
    return game["ats"] == game["hts"]


def get_message(game):
    away = teams[game["atv"]]
    home = teams[game["htv"]]
    message = messages["default"].format(
        away["handle"],
        home["handle"],
        game["hts"]
    )

    return message


def tweet(game):
    print(get_message(game))


def check_games():
    games = fetch_games()
    for game in games:
        if is_tied(game) and is_overtime(game):
            tweet(game)
