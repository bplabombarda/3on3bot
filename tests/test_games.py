import json

from bot.games import is_overtime, is_tied, fetch_games, \
    get_ot_games, parse_response
from .mock_games import *


class MockRes:
    def __init__(self):
        self.text = "bunchaGames({\"games\":[{\"id\":1}]})"


def test_parse_response():
    res = MockRes()
    expected = json.loads("[{\"id\":1}]")
    result = parse_response(res)

    assert result == expected


def test_fetch_games():
    assert True


class TestIsOverTime:
    def test_end_of_third(self):
        result = is_overtime(mock_end_third)
        assert result == True

    def test_overtime(self):
        result = is_overtime(mock_overtime)
        assert result == True

    def test_not_live(self):
        result = is_overtime(mock_not_live)
        assert result == False


class TestIsTied:
    def test_tied(self):
        result = is_tied(mock_tied)
        assert result == True

    def test_not_tied(self):
        result = is_tied(mock_not_tied)
        assert result == False
