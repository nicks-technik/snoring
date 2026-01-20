"""X.com (Twitter) notifier module for alerts."""

import logging
import tweepy
from datetime import datetime

logger = logging.getLogger(__name__)

class XNotifier:
    """Sends alerts via X.com (Twitter) Tweets."""

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        access_token: str,
        access_token_secret: str,
        recipient_id: str
    ):
        """Initializes the X.com notifier.

        Args:
            api_key: X.com API Consumer Key.
            api_secret: X.com API Consumer Secret.
            access_token: X.com User Access Token.
            access_token_secret: X.com User Access Token Secret.
            recipient_id: Ignored in tweet mode, but kept for interface compatibility.
        """
        self.recipient_id = recipient_id
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def send_alert(self, message: str):
        """Sends a synchronous alert message via X.com Tweet.

        Args:
            message: The message text to send.
        """
        try:
            # Add timestamp to ensure uniqueness
            timestamp = datetime.now().strftime('%H:%M:%S')
            tweet_text = f"[{timestamp}] {message}"
            
            self.client.create_tweet(text=tweet_text)
            logger.info(f"X.com alert sent: {tweet_text}")
        except Exception as e:
            logger.error(f"Failed to send X.com alert: {e}")

