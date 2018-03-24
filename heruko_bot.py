# Dependencies

import tweepy
import time
import json
import random
import os


# Twitter API Keys. Place your keys here.
consumer_key= os.environ['consumer_key']
consumer_secret= os.environ['consumer_secret']
access_token= os.environ['access_token']
access_token_secret= os.environ['access_token_secret']




# Quotes to Tweet
happy_quotes = [
    "Working on Heruko bot",
    "Tweets are sent by heroku automatically "
    ]


# Create function for tweeting
def HappyItUp():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)


