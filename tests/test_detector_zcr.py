import unittest.mock as mock
import pytest
from snoring.detector import SnoreDetector

@pytest.mark.asyncio
async def test_snore_detector_zcr_filtering():
    # Setup
    mock_recorder = mock.Mock()
    mock_recorder.read_chunk.return_value = b'\x00' * 1024 # Dummy data
    
    # Mock audio_utils functions
    with mock.patch('snoring.detector.calculate_rms') as mock_rms, \
         mock.patch('snoring.detector.calculate_zcr') as mock_zcr:
        
        # Case 1: RMS high, ZCR low (Snore) -> Should detect
        mock_rms.return_value = 1000.0 # > threshold
        mock_zcr.return_value = 0.05   # < zcr_threshold
        
        callback = mock.Mock()
        detector = SnoreDetector(
            recorder=mock_recorder,
            threshold=500.0,
            on_detection=callback,
            zcr_threshold=0.1
        )
        
        await detector.step_async()
        callback.assert_called_once()
        
        # Case 2: RMS high, ZCR high (Noise/Speech) -> Should NOT detect
        mock_rms.return_value = 1000.0
        mock_zcr.return_value = 0.2    # > zcr_threshold
        callback.reset_mock()
        
        await detector.step_async()
        callback.assert_not_called()
        
        # Case 3: RMS low (Silence) -> Should NOT detect regardless of ZCR
        mock_rms.return_value = 100.0
        mock_zcr.return_value = 0.05
        callback.reset_mock()
        
        await detector.step_async()
        callback.assert_not_called()

def test_snore_detector_init_zcr_threshold():
    mock_recorder = mock.Mock()
    detector = SnoreDetector(recorder=mock_recorder, threshold=100.0, zcr_threshold=0.2)
    assert detector.zcr_threshold == 0.2
