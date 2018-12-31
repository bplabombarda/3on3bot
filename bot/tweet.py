import json
import re

import requests
import tweepy

from .messages import messages
from .teams import teams

url = "http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
                            AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/47.0.2526.106 Safari/537.36"
}
res = requests.get(url, headers=headers)


def games_from_response():
    pattern = r"\{(?:{[^{}]*}|[^{}])*}"
    matches = re.finditer(pattern, res.text, re.MULTILINE)
    results = [match.group() for match in matches]
    json_data = json.loads(results[0])
    return json_data["games"]


def parse_games():
    games = games_from_response()
    return games


def game_is_ot(game):
    return


def tweet_game():
    return
