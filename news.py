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
