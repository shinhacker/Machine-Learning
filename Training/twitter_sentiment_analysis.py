#Author      : Shin McCold
#Challenge 2 : Machine Learning with python 
#Objective   : Twitter Sentiment Analysis
#Credits     : Thanks @Siraj Raval

import tweepy                   #Twitter API for Python
from textblob import TextBlob   #Python sentiment lib

consumer_key = 'Your Consumer Key'
consumer_secret = 'Your Consumer Secret'

access_token = 'Your Access Token'
access_token_secret = 'Your Access Token Secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('learn')   #Searing Specify tweets

for tweet in public_tweets:
    print(tweet.text)                 #Print those tweets
    analysis=TextBlob(tweet.text)     #Do the sentiment Analysis
    print analysis.sentiment          #Print the result
