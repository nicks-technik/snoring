import unittest.mock as mock
import pytest
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.FritzNotifier')
@mock.patch('snoring.cli.LineNotifier')
@mock.patch('snoring.cli.XNotifier')
@mock.patch('snoring.cli.SnoreDetector')
@mock.patch('snoring.cli.os.getenv')
async def test_cli_x_notifier_integration(mock_getenv, mock_detector, mock_x, mock_line, mock_fritz, mock_telegram, mock_recorder, mock_dotenv):
    # Setup returns for getenv
    def getenv_side_effect(key, default=None):
        vals = {
            "TELEGRAM_BOT_TOKEN": "t",
            "TELEGRAM_CHAT_ID": "c",
            "X_ENABLED": "True",
            "X_API_KEY": "ak",
            "X_API_SECRET": "as",
            "X_ACCESS_TOKEN": "at",
            "X_ACCESS_SECRET": "axs",
            "X_RECIPIENT_ID": "rid"
        }
        return vals.get(key, default)
    
    mock_getenv.side_effect = getenv_side_effect
    mock_detector.return_value.start_loop_async = mock.AsyncMock()
    
    await run_app()
    
    # Verify XNotifier was instantiated
    mock_x.assert_called_once_with(
        api_key="ak",
        api_secret="as",
        access_token="at",
        access_token_secret="axs",
        recipient_id="rid"
    )
    
    # Verify it was added to the notifiers list in correct order
    notifiers = mock_detector.call_args[1]['notifier']
    # Notifiers are: Telegram (index 0), X (index 1)
    assert mock_x.return_value == notifiers[1]

