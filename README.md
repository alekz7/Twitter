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

The script expects your Twitter API credentials to be set as environment variables. You can provide these by creating a `.env` file in the project root:

1. Copy the example file:

```bash
cp .env.example .env
```

2. Edit the `.env` file and fill in your credentials:
   - `CONSUMER_KEY`: Your Twitter API Key
   - `CONSUMER_KEY_SECRET`: Your Twitter API Secret Key
   - `ACCESS_TOKEN`: Your Access Token
   - `ACCESS_TOKEN_SECRET`: Your Access Token Secret

Alternatively, you can export them directly in your shell:

```bash
# Windows (PowerShell)
$env:CONSUMER_TOKEN="your_key"
# macOS/Linux
export CONSUMER_TOKEN="your_key"
```

## Usage

Run the script by providing a search query:

```bash
python Sentiment.py --query "Python"
```

The script will fetch recent tweets and display their sentiment (Polarity and Subjectivity).
