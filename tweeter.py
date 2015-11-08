import requests
import tweepy
from bs4 import BeautifulSoup

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
                        ACCESS_TOKEN_SECRET, URL, HASHTAG

# --- MOVE TO CONFIG --------------------------------------------------

# --- END MOVE TO CONFIG ----------------------------------------------

# =====================================================================
# Auth Twitter API Kajigger & create API refernce Kajigger
# =====================================================================
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# =====================================================================
# Get HTML content
# =====================================================================
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
scores = soup.select(".game-card-container")
homeTeamText = soup.select("")
awayTeamText = soup.select("")


# =====================================================================
# Check Scores: takes *scores* - a bs4 tag object.
# Czechs text for which period ended. If 3rd, tweets which game.
# =====================================================================
def check_scores(scores):
    for score in scores:
        # Grab node with period-end class;
        # this contains the end of period status.
        game_timer = score.find_all(class_="period-end")

        process_score_text(game_timer)


# =====================================================================
# Post (Tweet) Game
# =====================================================================
def process_score_text(score_nodes):
    # =================================================================
    # Since there may be multiple games returned
    # we will iterate over our results.
    # =================================================================
    for child in score_nodes:
        # NOTE: Testing; please get rid of me later
        print(child.text)

        if child.text:
            period_status = child.text.split()
            # NOTE: Testing; please get rid of me later
            print(period_status)

            if period_status[0] == 'End' and period_status[1] =='3RD':
                # =====================================================
                # Build status
                # =====================================================
                status = str(awayTeam) + " vs " \
                            + str(homeTeam) + "#" + HASHTAG

                # =====================================================
                # Post status (tweet)
                # =====================================================
                api.update_status(status=status)
                # NOTE: Testing; please get rid of me later
                print(status)


                # NOTE: Testing; please get rid of me later
                print("Overtime!")

            else:
                # NOTE: Testing; please get rid of me later
                print("Nooovertime :(((")


check_scores(scores)
