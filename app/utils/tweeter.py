import tweepy
import requests
from bs4 import BeautifulSoup


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

res = requests.get('http://www.sportsnet.ca/hockey/nhl/scores/')
soup = BeautifulSoup(res.text, 'html.parser')

# Grab all game cards elements from the soup
game_cards = soup.find_all(class_='game-card-container')


def parse_game(game_card, api):

    # Game ID
    game_id = game_card.attrs['id'].split('_')[3]
    # print(game_id)

    # Game Info
    game_start = game_card.find(class_='game-time-start')
    game_status = game_card.find(class_='scores-game-status')
    game_progress = game_status.find(class_="game-current-time")
    game_period = game_status.find(class_="game-current-period")
    period_end = game_status.select('.period_end > strong')
    overtime = game_card.select('.scores-game-status td')
    game_final = game_card.find(class_='final')

    # Away Team Info
    away_team_info = game_card.find(class_='team-container-1')
    away_team_city = away_team_info.text.strip('\n').split('\n')[2]
    away_team_name = away_team_info.text.strip('\n').split('\n')[3]
    away_team_logo = away_team_info.select(
                        '.scores-team-logo img')[0].attrs['src']
    away_team_score = away_team_info.find(class_='scores-team-score')

    # Home Team Info
    home_team_info = game_card.find(class_='team-container-2')
    home_team_city = home_team_info.text.strip('\n').split('\n')[2]
    home_team_name = home_team_info.text.strip('\n').split('\n')[3]
    home_team_logo = home_team_info.select(
                        '.scores-team-logo img')[0].attrs['src']
    home_team_score = home_team_info.find(class_='scores-team-score')

    if game_period != None:
        print(game_period.text)
        print(game_progress.text)
        if (game_period.text == 'OT') or (game_period.text == '3RD'):
            print('Overtime!')
        else:
            print('Nooovertime!')

    if len(period_end):
        print(period_end[0])

    if game_start != None:
        print(game_start.text)

    if game_final != None:
        print(game_final.text)



    tweet_game(overtime, away_team_name, away_team_score,
                    home_team_name, home_team_score)


def tweet_game(overtime, away_team_name, away_team_score,
                home_team_name, home_team_score):

    if home_team_score and away_team_score:
        print(home_team_score.text.strip(' '), away_team_score.text.strip(' '))
    # if overtime:
    status = away_team_name + " @ " + home_team_name + " #3on3bot"
    print(status)
    # api.update_status(status)


# Loop over game cards
for card in game_cards:
    parse_game(card, api)
