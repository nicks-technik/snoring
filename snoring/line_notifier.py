"""LINE notifier module for alerts."""

import logging
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    PushMessageRequest,
    TextMessage
)

logger = logging.getLogger(__name__)

class LineNotifier:
    """Sends alerts via LINE Messaging API."""

    def __init__(self, access_token: str, channel_secret: str, user_id: str):
        """Initializes the LINE notifier.

        Args:
            access_token: LINE Channel Access Token.
            channel_secret: LINE Channel Secret.
            user_id: LINE User ID to send messages to.
        """
        self.user_id = user_id
        self.configuration = Configuration(access_token=access_token)
        # channel_secret is not directly needed for push_message in v3 messaging api
        # but kept for consistency if needed later for signature validation etc.
        self.channel_secret = channel_secret
        self.api_client = ApiClient(self.configuration)
        self.messaging_api = MessagingApi(self.api_client)

    def send_alert(self, message: str):
        """Sends a synchronous alert message via LINE.

        Args:
            message: The message text to send.
        """
        try:
            push_message_request = PushMessageRequest(
                to=self.user_id,
                messages=[TextMessage(text=message)]
            )
            self.messaging_api.push_message(push_message_request)
            logger.info(f"LINE alert sent: {message}")
        except Exception as e:
            logger.error(f"Failed to send LINE alert: {e}")
