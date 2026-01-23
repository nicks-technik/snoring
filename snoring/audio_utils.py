"""Audio utility functions for snoring detection."""

import numpy as np
import librosa

def calculate_rms(audio_chunk: bytes) -> float:
    """Calculates the Root Mean Square (RMS) of an audio chunk.

    RMS is a measure of the average power of the audio signal.

    Args:
        audio_chunk: Raw audio data as bytes (16-bit PCM).

    Returns:
        The RMS value as a float.
    """
    try:
        # Convert bytes to numpy array of 16-bit integers
        data = np.frombuffer(audio_chunk, dtype=np.int16)
    except (ValueError, TypeError):
        # Handle cases where buffer size is not a multiple of 2 or not bytes
        return 0.0
    
    if data.size == 0:
        return 0.0
        
    # Calculate RMS: sqrt(mean(squares))
    # Using float64 for intermediate calculation to avoid overflow
    return float(np.sqrt(np.mean(data.astype(np.float64)**2)))

def calculate_zcr(audio_chunk: bytes) -> float:
    """Calculates the average Zero-Crossing Rate (ZCR) of an audio chunk.

    ZCR is the rate at which the signal changes sign. Snoring typically
    has a lower ZCR compared to speech or noise.

    Args:
        audio_chunk: Raw audio data as bytes (16-bit PCM).

    Returns:
        The average ZCR as a float (0.0 to 1.0).
    """
    try:
        # Convert bytes to numpy array of floats (normalized to -1.0 to 1.0)
        data = np.frombuffer(audio_chunk, dtype=np.int16).astype(np.float32) / 32768.0
    except (ValueError, TypeError):
        return 0.0
        
    if data.size == 0:
        return 0.0
        
    # librosa.feature.zero_crossing_rate returns a 2D array [1, num_frames]
    # We take the mean across frames to get a single value for the chunk
    zcr_series = librosa.feature.zero_crossing_rate(y=data, frame_length=data.size, hop_length=data.size)
    return float(np.mean(zcr_series))

def calculate_spectral_centroid(audio_chunk: bytes, sample_rate: int) -> float:
    """Calculates the spectral centroid of an audio chunk.

    The spectral centroid indicates where the "center of mass" of the spectrum is.
    Snoring typically has more low-frequency energy, resulting in a lower centroid.

    Args:
        audio_chunk: Raw audio data as bytes (16-bit PCM).
        sample_rate: The sample rate of the audio (e.g., 44100).

    Returns:
        The spectral centroid in Hz.
    """
    try:
        # Convert bytes to numpy array of floats (normalized)
        data = np.frombuffer(audio_chunk, dtype=np.int16).astype(np.float32) / 32768.0
    except (ValueError, TypeError):
        return 0.0
        
    if data.size == 0:
        return 0.0
        
    # librosa.feature.spectral_centroid returns a 2D array [1, num_frames]
    # We use a large frame length to cover the chunk if possible, or let librosa handle frames
    # Given we analyze chunks, we can just take the mean of the frames in this chunk.
    # Note: spectral_centroid requires a sampling rate (sr).
    centroids = librosa.feature.spectral_centroid(y=data, sr=sample_rate)
    
    return float(np.mean(centroids))