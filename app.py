import requests
import tweepy
from bs4 import BeautifulSoup

# --- MOVE TO CONFIG --------------------------------------------------
# =====================================================================
# Twitter API Kajigger
# =====================================================================
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

url = 'http://www.sportsnet.ca/hockey/nhl/scores/'
# --- END MOVE TO CONFIG ----------------------------------------------

# =====================================================================
# Auth Twitter API Kajigger & create API refernce Kajigger
# =====================================================================
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

awayTeam = "NYI"
homeTeam = "NYR"

status = str(awayTeam) + " vs " + str(homeTeam) + " #3on3"
print(status)
# api.update_status(status=status)

# =====================================================================
# Get HTML content
# =====================================================================
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
scores = soup.select(".game-card-container")


# =====================================================================
# Check Scores: takes *scores* - a bs4 tag object.
# Czechs text for which period ended. If 3rd, tweets which game.
# =====================================================================
def check_scores(scores):
    for score in scores:
        game_time = score.find_all(class_="period-end")
        print(game_time, type(game_time))

        for child in game_time:

            if child.text:
                period_status = child.text.split()

                # if period_status[0] == 'End' and period_status[1] =='3RD':
                if period_status[0] == 'End':
                    print("Overtime!")
                    status = str(awayTeam) + " vs " + str(homeTeam) + " #3on3"
                    api.update_status(status=status)
                    print(status)
                else:
                    print("Nooovertime :(((")

                print(period_status)

            print(child.text)

            
check_scores(scores)
