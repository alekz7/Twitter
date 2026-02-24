# Twitter Sentiment Analysis

A simple Python script to perform sentiment analysis on tweets using the Twitter API and TextBlob.

## Prerequisites

Before running the script, you need to:
1. Create a Twitter Developer account at [developer.twitter.com](https://developer.twitter.com/).
2. Create an application to obtain your API credentials.
3. (Optional but recommended) Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

## Setup

Set the following environment variables with your Twitter API credentials:

* `CONSUMER_TOKEN`: Your Twitter API Key
* `CONSUMER_SECRET`: Your Twitter API Secret Key
* `ACCESS_TOKEN`: Your Access Token
* `ACCESS_TOKEN_SECRET`: Your Access Token Secret

## Usage

Run the script by providing a search query:

```bash
python Sentiment.py --query "Python"
```

The script will fetch recent tweets and display their sentiment (Polarity and Subjectivity).
