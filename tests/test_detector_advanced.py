import unittest.mock as mock
import pytest
from snoring.detector import SnoreDetector

def test_detector_spectral_centroid_filtering():
    """Test that high spectral centroid prevents detection even if RMS/ZCR are valid."""
    mock_recorder = mock.Mock()
    mock_recorder.read_chunk.return_value = b'some_audio'
    
    # Setup mocks for audio utils
    with mock.patch('snoring.detector.calculate_rms') as mock_rms, \
         mock.patch('snoring.detector.calculate_zcr') as mock_zcr, \
         mock.patch('snoring.detector.calculate_spectral_centroid') as mock_centroid:
        
        # Scenario: Valid snore RMS & ZCR, but HIGH Centroid (e.g. 3000Hz)
        mock_rms.return_value = 2000.0  # > threshold
        mock_zcr.return_value = 0.05    # < threshold
        mock_centroid.return_value = 3000.0 # > 1500Hz default threshold
        
        detector = SnoreDetector(
            recorder=mock_recorder,
            threshold=1000.0,
            spectral_centroid_threshold=1500.0, # New param
            min_consecutive_chunks=1            # Immediate trigger for this test
        )
        
        detected = detector.step()
        
        assert not detected, "Should be filtered by high spectral centroid"

def test_detector_consecutive_chunks_logic():
    """Test that detection only triggers after N consecutive valid chunks."""
    mock_recorder = mock.Mock()
    mock_recorder.read_chunk.return_value = b'some_audio'
    
    callback = mock.Mock()
    
    with mock.patch('snoring.detector.calculate_rms') as mock_rms, \
         mock.patch('snoring.detector.calculate_zcr') as mock_zcr, \
         mock.patch('snoring.detector.calculate_spectral_centroid') as mock_centroid:
        
        # Valid snore parameters
        mock_rms.return_value = 2000.0
        mock_zcr.return_value = 0.05
        mock_centroid.return_value = 500.0 # Low centroid
        
        detector = SnoreDetector(
            recorder=mock_recorder,
            threshold=1000.0,
            spectral_centroid_threshold=1500.0,
            min_consecutive_chunks=3,
            on_detection=callback
        )
        
        # Chunk 1: Valid
        assert not detector.step()
        callback.assert_not_called()
        
        # Chunk 2: Valid
        assert not detector.step()
        callback.assert_not_called()
        
        # Chunk 3: Valid -> Trigger!
        assert detector.step()
        callback.assert_called_once()

def test_detector_consecutive_chunks_reset():
    """Test that consecutive counter resets if a non-snore chunk interrupts."""
    mock_recorder = mock.Mock()
    mock_recorder.read_chunk.return_value = b'some_audio'
    
    callback = mock.Mock()
    
    with mock.patch('snoring.detector.calculate_rms') as mock_rms, \
         mock.patch('snoring.detector.calculate_zcr') as mock_zcr, \
         mock.patch('snoring.detector.calculate_spectral_centroid') as mock_centroid:
        
        detector = SnoreDetector(
            recorder=mock_recorder,
            threshold=1000.0,
            spectral_centroid_threshold=1500.0,
            min_consecutive_chunks=3,
            on_detection=callback
        )
        
        # Valid snore
        mock_rms.return_value = 2000.0
        mock_zcr.return_value = 0.05
        mock_centroid.return_value = 500.0
        
        # Chunk 1: Valid
        detector.step()
        
        # Chunk 2: INVALID (Low RMS)
        mock_rms.return_value = 500.0
        detector.step()
        
        # Reset RMS back to Valid
        mock_rms.return_value = 2000.0
        
        # Chunk 3 (should be treated as #1 again): Valid
        assert not detector.step()
        callback.assert_not_called()
        
        # Chunk 4 (treated as #2): Valid
        assert not detector.step()
        
        # Chunk 5 (treated as #3): Valid -> Trigger
        assert detector.step()
        callback.assert_called_once()
