import json

from bot.utils import fetch_games, parse_response


class MockRes:
    def __init__(self):
        self.text = "bunchaGames({\"games\":[{\"id\":1}]})"


def test_parse_response():
    res = MockRes()
    expected = json.loads("[{\"id\":1}]")
    result = parse_response(res)

    assert result == expected
