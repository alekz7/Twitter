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
        # API v2 usually requires Bearer Token for searches
        bearer_token        = os.environ.get('BEARER_TOKEN')
        consumer_key        = os.environ['CONSUMER_KEY']
        consumer_secret     = os.environ['CONSUMER_KEY_SECRET']
        access_token        = os.environ['ACCESS_TOKEN']
        access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    except KeyError as e:
        print(f"Error: Environment variable {e} not set.")
        sys.exit(1)

    # Authentication (API v2 uses tweepy.Client)
    try:
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
    except Exception as e:
        print(f"Error: Client initialization failed. {e}")
        sys.exit(1)

    print(f"Searching for: {args.query}...\n")

    try:
        # Fetch tweets using API v2 (search_recent_tweets)
        # Note: Free tier has strict limits on query complexity
        response = client.search_recent_tweets(query=args.query, max_results=args.count)
        
        if response.data:
            for tweet in response.data:
                print(f"Tweet: {tweet.text}")
                analysis = tb(tweet.text)
                sentiment = analysis.sentiment
                label = get_sentiment_label(sentiment.polarity)
                
                print(f"Sentiment: {label} (Polarity: {sentiment.polarity:.2f}, Subjectivity: {sentiment.subjectivity:.2f})")
                print("-" * 30)
        else:
            print("No tweets found or access limited.")
            
    except Exception as e:
        print(f"Error fetching tweets: {e}")

if __name__ == "__main__":
    main()
