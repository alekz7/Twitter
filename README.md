# Twitter Sentiment Analysis

A simple Python script to perform sentiment analysis on tweets using the Twitter API v2 and TextBlob.

## Prerequisites

Before running the script, you need to:

1. **Twitter Developer Account:** Create one at [developer.twitter.com](https://developer.twitter.com/).
2. **Create a Project:** In the Developer Portal, you **must** create a "Project" first.
3. **App within Project:** Create a new App inside that Project or move an existing one into it. API v2 search will not work with "Standalone Apps".
4. **Permissions:** Ensure your App has "Read" permissions enabled.
5. **Virtual Environment (Recommended):**

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

6. **Install Dependencies:**

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

## Setup

The script expects your Twitter API credentials to be set as environment variables.

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit the `.env` file and fill in your credentials from the **Keys and Tokens** tab of your App:
   - `BEARER_TOKEN`: Found under "Authentication Tokens". **Required for v2 search.**
   - `CONSUMER_KEY`: API Key.
   - `CONSUMER_KEY_SECRET`: API Key Secret.
   - `ACCESS_TOKEN`: Access Token.
   - `ACCESS_TOKEN_SECRET`: Access Token Secret.

## Usage

Run the script by providing a search query:

```bash
python Sentiment.py --query "Python"
```

The script will fetch recent tweets using API v2 and display their sentiment (Polarity and Subjectivity).
