"""Audio utility functions for snoring detection."""

import numpy as np

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