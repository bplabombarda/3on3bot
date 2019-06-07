import time

from bot.scheduler import CustomScheduler
from bot.tweet import tweet_game

scheduler = CustomScheduler()

scheduler.every(1).minute.do(tweet_game)

while True:
    scheduler.run_pending()
    time.sleep(1)
