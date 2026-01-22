import pytest
import numpy as np
from snoring.audio_utils import calculate_spectral_centroid

def test_calculate_spectral_centroid_low_frequency():
    # Generate a sine wave at 440Hz
    sample_rate = 44100
    duration = 0.1
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # 440Hz sine wave
    audio_data = (np.sin(2 * np.pi * 440 * t) * 32767).astype(np.int16)
    audio_bytes = audio_data.tobytes()

    centroid = calculate_spectral_centroid(audio_bytes, sample_rate)
    
    # Ideally, for a pure tone, the centroid should be close to the frequency
    # Allowing some margin due to spectral leakage / windowing
    assert 400 < centroid < 600

def test_calculate_spectral_centroid_high_frequency():
    # Generate a sine wave at 5000Hz
    sample_rate = 44100
    duration = 0.1
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # 5000Hz sine wave
    audio_data = (np.sin(2 * np.pi * 5000 * t) * 32767).astype(np.int16)
    audio_bytes = audio_data.tobytes()

    centroid = calculate_spectral_centroid(audio_bytes, sample_rate)
    
    assert 4800 < centroid < 5200

def test_calculate_spectral_centroid_silence():
    sample_rate = 44100
    audio_bytes = b'\x00' * 2048
    centroid = calculate_spectral_centroid(audio_bytes, sample_rate)
    assert centroid == 0.0
