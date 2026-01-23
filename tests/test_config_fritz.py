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
async def test_fritz_enabled_flag(mock_getenv, mock_detector, mock_line, mock_fritz, mock_telegram, mock_recorder, mock_dotenv):
    # Case 1: FRITZ_ENABLED = True
    def getenv_side_effect_true(key, default=None):
        vals = {
            "TELEGRAM_BOT_TOKEN": "t",
            "TELEGRAM_CHAT_ID": "c",
            "FRITZ_ENABLED": "True",
            "FRITZ_ADDRESS": "1.2.3.4",
            "FRITZ_USER": "u",
            "FRITZ_PASSWORD": "p",
            "FRITZ_TARGET_NUMBER": "t"
        }
        return vals.get(key, default)
    
    mock_getenv.side_effect = getenv_side_effect_true
    mock_detector.return_value.start_loop_async = mock.AsyncMock()
    
    await run_app()
    
    mock_fritz.assert_called_once()
    
    # Case 2: FRITZ_ENABLED = False
    mock_fritz.reset_mock()
    mock_detector.reset_mock()
    
    def getenv_side_effect_false(key, default=None):
        vals = {
            "TELEGRAM_BOT_TOKEN": "t",
            "TELEGRAM_CHAT_ID": "c",
            "FRITZ_ENABLED": "False",
            "FRITZ_ADDRESS": "1.2.3.4", 
            # Address present but flag is false
        }
        return vals.get(key, default)

    mock_getenv.side_effect = getenv_side_effect_false
    mock_detector.return_value.start_loop_async = mock.AsyncMock()

    await run_app()

    mock_fritz.assert_not_called()

    # Case 3: FRITZ_ENABLED missing (default False)
    mock_fritz.reset_mock()
    
    def getenv_side_effect_missing(key, default=None):
        vals = {
            "TELEGRAM_BOT_TOKEN": "t",
            "TELEGRAM_CHAT_ID": "c",
            "FRITZ_ADDRESS": "1.2.3.4",
        }
        return vals.get(key, default)

    mock_getenv.side_effect = getenv_side_effect_missing
    mock_detector.return_value.start_loop_async = mock.AsyncMock()

    await run_app()

    mock_fritz.assert_not_called()
