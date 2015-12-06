import tweepy
import requests
from bs4 import BeautifulSoup


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

res = requests.get('http://www.sportsnet.ca/hockey/nhl/scores/')
soup = BeautifulSoup(res.text, 'html.parser')

game_cards = soup.find_all(class_='game-card-container')

# print(game_cards[0].attrs['id'].split('_')[3])

def tweet3on3(game_card, api):

    # Game ID
    game_id = game_card.attrs['id'].split('_')[3]
    print(game_id)

    # Game Info
    game_status = game_card.find(class_='scores-game-status')
    print(game_status)

    # Away Team Info
    game_status = game_card.find(class_='team-container-1')

    # Home Team Info
    game_status = game_card.find(class_='team-container-2')

    # away_team = ""
    # home_team = ""
    #
    # status = away_team + " @ " + home_team + " #3on3bot"
    # api.update_status(status)


for card in game_cards:
    tweet3on3(card, api)
