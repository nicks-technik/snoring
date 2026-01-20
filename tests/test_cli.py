import unittest.mock as mock
import pytest
import asyncio
import os
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.SnoreDetector')
async def test_cli_run_app_success(mock_detector_class, mock_notifier_class, mock_recorder_class, mock_dotenv):
    with mock.patch.dict('os.environ', {
        'TELEGRAM_BOT_TOKEN': 'test_token',
        'TELEGRAM_CHAT_ID': 'test_chat_id',
        'SENSITIVITY_THRESHOLD': '1000.0'
    }):
        # Reset mocks to clear any calls during import/setup if any
        mock_detector_class.reset_mock()
        mock_notifier_class.reset_mock()
        mock_recorder_class.reset_mock()
        
        mock_detector_class.return_value.start_loop_async = mock.AsyncMock()
        
        await run_app()
        
        mock_recorder_class.assert_called_once()
        mock_notifier_class.assert_called_once_with(token='test_token', chat_id='test_chat_id')
        mock_detector_class.assert_called_once_with(
            recorder=mock_recorder_class.return_value,
            threshold=1000.0,
            notifier=mock_notifier_class.return_value
        )
        mock_detector_class.return_value.start_loop_async.assert_called_once()
        mock_recorder_class.return_value.close.assert_called_once()

@pytest.mark.asyncio
@mock.patch('snoring.cli.os.getenv')
async def test_cli_run_app_missing_env(mock_getenv):
    # Mocking side effect to return None for token/chat_id
    def getenv_side_effect(key, default=None):
        if key in ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]:
            return None
        return default
    mock_getenv.side_effect = getenv_side_effect
    
    with mock.patch('snoring.cli.logging.error') as mock_log_error:
        await run_app()
        mock_log_error.assert_called_with("Telegram token or Chat ID not found in environment.")

def test_cli_main_keyboard_interrupt():
    with mock.patch('snoring.cli.asyncio.run', side_effect=KeyboardInterrupt):
        from snoring.cli import main
        main() # Should not raise
