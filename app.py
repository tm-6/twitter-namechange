import tweepy
from datetime import datetime
import os

API_Key = os.environ['API_Key']
API_Key_Secret = os.environ['API_Key_Secret']
Access_Token = os.environ['Access_Token']
Access_Token_Secret = os.environ['Access_Token_Secret']

auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)
api = tweepy.API(auth)

def name_change():
    end_day = datetime(2022,6,8)
    today = datetime.now()

    day = end_day - today
    day = day.days # + 1 HerokuがUTCしか選択できないので + 1 は無し

    api.update_profile(name = f'うえとも@{day}日後までにエンジニア転職！')

app = name_change()

server = app.server
