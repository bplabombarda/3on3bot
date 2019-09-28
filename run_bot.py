import logging

from bot.tweet import tweet_ot_games

logger = logging.getLogger(__name__)


def run_bot():
    try:
        tweet_ot_games()
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    run_bot()
