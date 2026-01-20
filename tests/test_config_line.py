import unittest.mock as mock
import pytest
import os
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.FritzNotifier')
@mock.patch('snoring.cli.SnoreDetector')
@mock.patch('snoring.cli.os.getenv')
async def test_cli_loads_line_config(mock_getenv, mock_detector, mock_fritz, mock_telegram, mock_recorder, mock_dotenv):
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
    
    # Verify LINE vars were requested
    calls = [call[0][0] for call in mock_getenv.call_args_list]
    assert "LINE_ENABLED" in calls
    assert "LINE_CHANNEL_ACCESS_TOKEN" in calls
    assert "LINE_CHANNEL_SECRET" in calls
    assert "LINE_USER_ID" in calls
