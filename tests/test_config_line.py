import unittest.mock as mock
import pytest
import os
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.FritzNotifier')
@mock.patch('snoring.cli.LineNotifier')
@mock.patch('snoring.cli.SnoreDetector')
@mock.patch('snoring.cli.os.getenv')
async def test_cli_instantiates_line_notifier(mock_getenv, mock_detector, mock_line, mock_fritz, mock_telegram, mock_recorder, mock_dotenv):
    # Setup default returns for getenv
    def getenv_side_effect(key, default=None):
        vals = {
            "TELEGRAM_BOT_TOKEN": "t",
            "TELEGRAM_CHAT_ID": "c",
            "LINE_ENABLED": "True",
            "LINE_CHANNEL_ACCESS_TOKEN": "token",
            "LINE_CHANNEL_SECRET": "secret",
            "LINE_USER_ID": "uid"
        }
        return vals.get(key, default)
    
    mock_getenv.side_effect = getenv_side_effect
    mock_detector.return_value.start_loop_async = mock.AsyncMock()
    
    await run_app()
    
    # Verify LINE notifier was instantiated with correct args
    mock_line.assert_called_once_with(
        access_token="token",
        channel_secret="secret",
        user_id="uid"
    )
    
    # Verify it was added to the detector
    notifiers = mock_detector.call_args[1]['notifier']
    assert mock_line.return_value in notifiers
