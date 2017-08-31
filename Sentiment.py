# This is the next example for python MachineLearning
# In this we are going to use the twitter Sentiment Analisis
# first step is make an account on twitter
# user name ingAlekz7
# application in twitter SentimentAlekz7
# Consumer Key (API Key)	
# Consumer Secret (API Secret)	
# Owner	ingAlekz7
# Access Token	
# Access Token Secret	

import tweepy
from textblob import TextBlob as tb

consumer_token 		= ''
consumer_secret 	= ''
access_token		= ''
access_token_secret	= ''

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('McGregor')

for tweet in public_tweets:
	print(tweet.text)
	analisis = tb(tweet.text)
	print(analisis.sentiment)
