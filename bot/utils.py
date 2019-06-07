import json
import os
import re
import sys

import requests

from bot.constants import HEADERS, PATTERN, SOURCE_URL


def parse_response(response):
    matches = re.finditer(PATTERN, response.text, re.MULTILINE)
    results = [match.group() for match in matches]
    json_data = json.loads(results[0])

    return json_data["games"]


def fetch_games():
    if os.environ["ENV"] == "mock":
        with open("../data/sample_games.json") as local_file:
            mock_json = json.load(local_file)

        return mock_json

    try:
        res = requests.get(SOURCE_URL, HEADERS)
        games = parse_response(res)

        return games
    except:
        print(sys.exc_info()[0])
