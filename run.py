import logging
import time

from bot.scheduler import CustomScheduler
from bot.tweet import tweet_ot_games

logger = logging.getLogger(__name__)
scheduler = CustomScheduler()


def run():
    try:
        tweet_ot_games()
    except Exception as e:
        logger.error(e)

scheduler.every(1).minute.do(run)

while True:
    scheduler.run_pending()
    time.sleep(1)
