"""X.com (Twitter) notifier module for alerts."""

import logging
import tweepy

logger = logging.getLogger(__name__)

class XNotifier:
    """Sends alerts via X.com (Twitter) Direct Messages."""

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
            recipient_id: Numeric User ID to send DMs to.
        """
        self.recipient_id = recipient_id
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def send_alert(self, message: str):
        """Sends a synchronous alert message via X.com DM.

        Args:
            message: The message text to send.
        """
        try:
            self.client.create_direct_message(
                participant_id=self.recipient_id,
                text=message
            )
            logger.info(f"X.com alert sent to {self.recipient_id}: {message}")
        except Exception as e:
            logger.error(f"Failed to send X.com alert: {e}")
