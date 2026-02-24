import os
import sys
import argparse
import tweepy
from textblob import TextBlob as tb
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def get_sentiment_label(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    parser = argparse.ArgumentParser(description='Twitter Sentiment Analysis')
    parser.add_argument('--query', type=str, default='McGregor', help='Search query for Twitter')
    parser.add_argument('--count', type=int, default=10, help='Number of tweets to fetch')
    args = parser.parse_args()

    # Load environment variables
    try:
        consumer_key      = os.environ['CONSUMER_KEY']
        consumer_key_secret     = os.environ['CONSUMER_KEY_SECRET']
        access_token        = os.environ['ACCESS_TOKEN']
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    except KeyError as e:
        print(f"Error: Environment variable {e} not set.")
        sys.exit(1)

    # Authentication
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        # Verify credentials
        api.verify_credentials()
    except Exception as e:
        print(f"Error: Authentication failed. {e}")
        sys.exit(1)

    print(f"Searching for: {args.query}...\n")

    try:
        # Fetch tweets
        public_tweets = api.search(q=args.query, count=args.count)

        for tweet in public_tweets:
            print(f"Tweet: {tweet.text}")
            analysis = tb(tweet.text)
            sentiment = analysis.sentiment
            label = get_sentiment_label(sentiment.polarity)
            
            print(f"Sentiment: {label} (Polarity: {sentiment.polarity:.2f}, Subjectivity: {sentiment.subjectivity:.2f})")
            print("-" * 30)
            
    except Exception as e:
        print(f"Error fetching tweets: {e}")

if __name__ == "__main__":
    main()
