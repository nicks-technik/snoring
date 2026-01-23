import unittest.mock as mock
import pytest
from snoring.telegram_notifier import TelegramNotifier
from telegram import Bot

@pytest.mark.asyncio
async def test_telegram_notifier_send_alert():
    with mock.patch('snoring.telegram_notifier.Bot') as mock_bot:
        bot_instance = mock_bot.return_value
        bot_instance.send_message = mock.AsyncMock()
        
        notifier = TelegramNotifier(token="fake_token", chat_id="fake_chat_id")
        await notifier.send_alert("Snoring detected!")
        
        mock_bot.assert_called_once_with(token="fake_token")
        bot_instance.send_message.assert_called_once_with(
            chat_id="fake_chat_id",
            text="Snoring detected!"
        )

@pytest.mark.asyncio
async def test_telegram_notifier_send_alert_failure():
    with mock.patch('snoring.telegram_notifier.Bot') as mock_bot:
        bot_instance = mock_bot.return_value
        bot_instance.send_message = mock.AsyncMock(side_effect=Exception("API Error"))
        
        notifier = TelegramNotifier(token="fake_token", chat_id="fake_chat_id")
        # Should not raise exception but log error
        await notifier.send_alert("Snoring detected!")
        
        bot_instance.send_message.assert_called_once()