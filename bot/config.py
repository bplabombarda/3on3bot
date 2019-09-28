import os


config = {
    "twitter_consumer_key": os.environ.get("TWITTER_CONSUMER_KEY", ""),
    "twitter_consumer_secret": os.environ.get("TWITTER_CONSUMER_SECRET", ""),
    "twitter_access_token": os.environ.get("TWITTER_ACCESS_TOKEN", ""),
    "twitter_access_token_secret": os.environ.get("TWITTER_ACCESS_TOKEN_SECRET", "")
}
