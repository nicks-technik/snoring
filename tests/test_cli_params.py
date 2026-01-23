import unittest.mock as mock
import pytest
from snoring.cli import run_app

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.SnoreDetector')
async def test_cli_passes_new_params(mock_detector_class, mock_telegram_class, mock_recorder_class, mock_dotenv):
    with mock.patch.dict('os.environ', {
        'TELEGRAM_ENABLED': 'True',
        'TELEGRAM_BOT_TOKEN': 'test_token',
        'TELEGRAM_CHAT_ID': 'test_chat_id',
        'SPECTRAL_CENTROID_THRESHOLD': '1800.0',
        'MIN_CONSECUTIVE_CHUNKS': '5'
    }):
        mock_detector_class.return_value.start_loop_async = mock.AsyncMock()
        
        await run_app()
        
        # Verify call args
        _, kwargs = mock_detector_class.call_args
        assert kwargs['spectral_centroid_threshold'] == 1800.0
        assert kwargs['min_consecutive_chunks'] == 5

@pytest.mark.asyncio
@mock.patch('snoring.cli.load_dotenv')
@mock.patch('snoring.cli.AudioRecorder')
@mock.patch('snoring.cli.TelegramNotifier')
@mock.patch('snoring.cli.SnoreDetector')
async def test_cli_defaults_for_new_params(mock_detector_class, mock_telegram_class, mock_recorder_class, mock_dotenv):
    with mock.patch.dict('os.environ', {
        'TELEGRAM_ENABLED': 'True',
        'TELEGRAM_BOT_TOKEN': 'test_token',
        'TELEGRAM_CHAT_ID': 'test_chat_id'
        # No new params set
    }):
        mock_detector_class.return_value.start_loop_async = mock.AsyncMock()
        
        await run_app()
        
        # Verify call args use defaults or are passed correctly if CLI sets them
        # If CLI sets them, we check what CLI passes.
        _, kwargs = mock_detector_class.call_args
        
        # Depending on implementation, CLI might pass explicit defaults or let detector handle it.
        # Ideally CLI should pass what it parsed.
        # Assuming CLI defaults to 1500.0 and 3
        assert kwargs.get('spectral_centroid_threshold', 1500.0) == 1500.0
        assert kwargs.get('min_consecutive_chunks', 3) == 3
