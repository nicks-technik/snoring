import unittest.mock as mock
import pytest
import numpy as np
from snoring.detector import SnoreDetector

def test_snore_detector_initialization():
    mock_recorder = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=1000.0)
    assert detector.threshold == 1000.0
    assert detector.recorder == mock_recorder

def test_snore_detector_step_no_detection():
    mock_recorder = mock.Mock()
    mock_recorder.read_chunk.return_value = b'\x00\x00' * 1024 # RMS 0
    
    callback = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=1000.0, on_detection=callback)
    
    detected = detector.step()
    
    assert not detected
    callback.assert_not_called()

def test_snore_detector_step_detection():
    mock_recorder = mock.Mock()
    # Constant value 2000 > threshold 1000
    chunk = np.array([2000] * 1024, dtype=np.int16).tobytes()
    mock_recorder.read_chunk.return_value = chunk
    
    callback = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=1000.0, on_detection=callback)
    
    detected = detector.step()
    
    assert detected
    callback.assert_called_once()

def test_snore_detector_start_loop_interrupted():
    mock_recorder = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=1000.0)
    
    # Side effect to raise KeyboardInterrupt
    with mock.patch.object(detector, 'step', side_effect=KeyboardInterrupt):
        detector.start_loop()
        detector.step.assert_called_once()

@pytest.mark.asyncio
async def test_snore_detector_multiple_notifiers():
    mock_recorder = mock.Mock()
    # RMS will be > 100
    chunk = np.array([500] * 1024, dtype=np.int16).tobytes()
    mock_recorder.read_chunk.return_value = chunk
    
    notifier1 = mock.AsyncMock()
    notifier2 = mock.AsyncMock()
    
    detector = SnoreDetector(
        recorder=mock_recorder, 
        threshold=100.0, 
        notifier=[notifier1, notifier2],
        cooldown_seconds=0
    )
    
    await detector.step_async()
    
    notifier1.send_alert.assert_called_once()
    notifier2.send_alert.assert_called_once()

@pytest.mark.asyncio
async def test_snore_detector_sync_and_async_notifiers():
    mock_recorder = mock.Mock()
    chunk = np.array([500] * 1024, dtype=np.int16).tobytes()
    mock_recorder.read_chunk.return_value = chunk
    
    async_notifier = mock.AsyncMock()
    sync_notifier = mock.Mock() # synchronous
    
    detector = SnoreDetector(
        recorder=mock_recorder, 
        threshold=100.0, 
        notifier=[async_notifier, sync_notifier],
        cooldown_seconds=0
    )
    
    await detector.step_async()
    
    async_notifier.send_alert.assert_called_once()
    sync_notifier.send_alert.assert_called_once()


