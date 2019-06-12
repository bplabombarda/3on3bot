import time

from bot.scheduler import CustomScheduler
from bot.tweet import tweet_ot_games

scheduler = CustomScheduler()

scheduler.every(1).minute.do(tweet_ot_games)

while True:
    scheduler.run_pending()
    time.sleep(1)
