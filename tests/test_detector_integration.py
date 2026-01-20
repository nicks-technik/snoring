import unittest.mock as mock
import pytest
import numpy as np
import time
from snoring.detector import SnoreDetector

@pytest.mark.asyncio
async def test_snore_detector_cooldown():
    mock_recorder = mock.Mock()
    # Constant value 2000 > threshold 1000
    chunk = np.array([2000] * 1024, dtype=np.int16).tobytes()
    mock_recorder.read_chunk.return_value = chunk
    
    mock_notifier = mock.Mock()
    mock_notifier.send_alert = mock.AsyncMock()
    
    # Cooldown 60 seconds
    detector = SnoreDetector(
        recorder=mock_recorder, 
        threshold=1000.0, 
        notifier=mock_notifier,
        cooldown_seconds=60
    )
    
    # First detection
    await detector.step_async()
    mock_notifier.send_alert.assert_called_once_with("Snoring detected! (RMS: 2000.00, ZCR: 0.0000)")
    
    # Second detection immediately after
    mock_notifier.send_alert.reset_mock()
    await detector.step_async()
    mock_notifier.send_alert.assert_not_called()
    
    # Fast forward time
    with mock.patch('snoring.detector.time.time', return_value=time.time() + 61):
        await detector.step_async()
        mock_notifier.send_alert.assert_called_once_with("Snoring detected! (RMS: 2000.00, ZCR: 0.0000)")

@pytest.mark.asyncio
async def test_snore_detector_start_loop_async_interrupted():
    mock_recorder = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=1000.0)
    
    with mock.patch.object(detector, 'step_async', side_effect=KeyboardInterrupt):
        await detector.start_loop_async()
        detector.step_async.assert_called_once()

@pytest.mark.asyncio
async def test_snore_detector_cooldown_logging():
    mock_recorder = mock.Mock()
    chunk = np.array([2000] * 1024, dtype=np.int16).tobytes()
    mock_recorder.read_chunk.return_value = chunk
    
    mock_notifier = mock.Mock()
    mock_notifier.send_alert = mock.AsyncMock()
    
    detector = SnoreDetector(
        recorder=mock_recorder, 
        threshold=1000.0, 
        notifier=mock_notifier,
        cooldown_seconds=60
    )
    
    await detector.step_async() # First alert
    
    with mock.patch('snoring.detector.logger') as mock_logger:
        await detector.step_async() # Second alert skipped
        mock_logger.debug.assert_called_with("Alert skipped due to cooldown.")
