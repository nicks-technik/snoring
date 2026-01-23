import unittest.mock as mock
import pytest
import asyncio
import os
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.FritzNotifier')
@mock.patch('snoring.cli.SnoreDetector')
async def test_cli_run_app_success(mock_detector_class, mock_fritz_class, mock_telegram_class, mock_recorder_class, mock_dotenv):
    with mock.patch.dict('os.environ', {
        'TELEGRAM_ENABLED': 'True',
        'TELEGRAM_BOT_TOKEN': 'test_token',
        'TELEGRAM_CHAT_ID': 'test_chat_id',
        'SENSITIVITY_THRESHOLD': '1000.0',
        'INTERVAL_SECONDS': '120',
        'FRITZ_ENABLED': 'True',
        'FRITZ_ADDRESS': '1.2.3.4',
        'FRITZ_USER': 'u',
        'FRITZ_PASSWORD': 'p',
        'FRITZ_TARGET_NUMBER': 't',
        'FRITZ_RING_DURATION': '5',
        'X_ENABLED': 'False',
        'LINE_ENABLED': 'False'
    }):
        # Reset mocks
        mock_detector_class.reset_mock()
        mock_telegram_class.reset_mock()
        mock_fritz_class.reset_mock()
        mock_recorder_class.reset_mock()
        
        mock_detector_class.return_value.start_loop_async = mock.AsyncMock()
        
        await run_app()
        
        mock_recorder_class.assert_called_once()
        mock_telegram_class.assert_called_once_with(token='test_token', chat_id='test_chat_id')
        mock_fritz_class.assert_called_once_with(
            address='1.2.3.4',
            user='u',
            password='p',
            target_number='t',
            ring_duration=5
        )
        
        # Check if both notifiers were passed in a list
        notifiers = mock_detector_class.call_args[1]['notifier']
        assert len(notifiers) == 2
        assert mock_telegram_class.return_value in notifiers
        assert mock_fritz_class.return_value in notifiers
        
        mock_detector_class.assert_called_once()
        mock_detector_class.return_value.start_loop_async.assert_called_once()
        mock_recorder_class.return_value.close.assert_called_once()

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.SnoreDetector')
async def test_cli_run_app_telegram_disabled(mock_detector_class, mock_telegram_class, mock_recorder_class, mock_dotenv):
    with mock.patch.dict('os.environ', {
        'TELEGRAM_ENABLED': 'False',
        'TELEGRAM_BOT_TOKEN': 'test_token',
        'TELEGRAM_CHAT_ID': 'test_chat_id'
    }):
        mock_detector_class.return_value.start_loop_async = mock.AsyncMock()
        await run_app()
        mock_telegram_class.assert_not_called()
        mock_detector_class.assert_called_once()

@pytest.mark.asyncio
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.os.getenv')
@mock.patch('snoring.cli.SnoreDetector')
@mock.patch('snoring.cli.TelegramNotifier')
async def test_cli_run_app_missing_env(mock_telegram, mock_detector, mock_getenv, mock_recorder):
    # Mocking side effect to return None for token/chat_id
    def getenv_side_effect(key, default=None):
        vals = {
            "TELEGRAM_ENABLED": "True",
            "TELEGRAM_BOT_TOKEN": None,
            "TELEGRAM_CHAT_ID": None
        }
        return vals.get(key, default)
    mock_getenv.side_effect = getenv_side_effect
    
    # Mock start_loop_async to return immediately
    mock_detector.return_value.start_loop_async = mock.AsyncMock()

    with mock.patch('snoring.cli.logging.error') as mock_log_error:
        await run_app()
        # It now continues after logging error, so we check if error was logged
        mock_log_error.assert_any_call("Telegram enabled but token or Chat ID not found in environment.")
        # Ensure detector started (even if notifier failed, the app might still start without it, or behave as designed)
        mock_detector.return_value.start_loop_async.assert_called_once()

def test_cli_main_keyboard_interrupt():
    with mock.patch('snoring.cli.asyncio.run', side_effect=KeyboardInterrupt):
        from snoring.cli import main
        main() # Should not raise
