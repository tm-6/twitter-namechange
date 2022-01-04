import json
import tweepy
from datetime import datetime

with open('secret.json') as f:
    secret = json.load(f)

auth = tweepy.OAuthHandler(secret['API_Key'], secret['API_Key_Secret'])
auth.set_access_token(secret['Access_Token'], secret['Access_Token_Secret'])
api = tweepy.API(auth)

def name_change():
    end_day = datetime(2022,6,8)
    today = datetime.now()

    day = end_day - today
    day = day.days + 1

    api.update_profile(name = f'うえとも@{day}日後までにエンジニア転職する')

app = name_change()

server = app.server
