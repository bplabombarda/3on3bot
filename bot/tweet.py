from bot.client import api
from bot.constants import STATUSES
from bot.games import get_ot_games
from bot.teams import teams


def get_status(game):
    away = teams[game["atv"]]
    home = teams[game["htv"]]
    score = game["hts"] if game["ats"] == game["hts"] else None

    return STATUSES["default"].format(
        away["handle"],
        home["handle"],
        game["hts"]
    )


def get_and_post_status(game):
    status = get_status(game)
    # api.update_status(status)
    print(status)


def tweet_ot_games():
    ot_games = get_ot_games()
    for game in ot_games:
        get_and_post_status(game)
