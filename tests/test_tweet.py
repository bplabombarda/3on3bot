from bot.tweet import get_status
from .mock_tweet import *


class TestGetStatus:
    def test_get_status_one(self):
        result = get_status(mock_game_one)
        expected = "@GoldenKnights at @SanJoseSharks tied at 0 going into #3on3OT"

        assert result == expected

    def test_get_status_two(self):
        result = get_status(mock_game_two)
        expected = "@GoldenKnights at @SanJoseSharks tied at 3 going into #3on3OT"

        assert result == expected

    def test_get_status_three(self):
        result = get_status(mock_game_three)
        expected = "@GoldenKnights at @SanJoseSharks tied at 99 going into #3on3OT"

        assert result == expected
