"""Telegram notifier module for alerts."""

import logging
from telegram import Bot

logger = logging.getLogger(__name__)

class TelegramNotifier:
    """Sends alerts via Telegram Bot API."""

    def __init__(self, token: str, chat_id: str):
        """Initializes the notifier.

        Args:
            token: Telegram Bot API token.
            chat_id: Telegram chat ID to send messages to.
        """
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=self.token)

    async def send_alert(self, message: str):
        """Sends an asynchronous alert message.

        Args:
            message: The message text to send.
        """
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
            logger.info(f"Telegram alert sent: {message}")
        except Exception as e:
            logger.error(f"Failed to send Telegram alert: {e}")
