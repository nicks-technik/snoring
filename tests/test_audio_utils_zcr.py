import numpy as np
import pytest
from snoring.audio_utils import calculate_zcr

def test_calculate_zcr_silence():
    chunk = b'\x00\x00' * 1024
    # librosa.feature.zero_crossing_rate on all zeros returns something close to 0
    assert calculate_zcr(chunk) == pytest.approx(0.0, abs=1e-5)

def test_calculate_zcr_sine_low():
    # Low frequency sine wave
    fs = 44100
    f = 100 # 100 Hz
    t = np.linspace(0, 1024/fs, 1024, endpoint=False)
    data = (np.sin(2 * np.pi * f * t) * 10000).astype(np.int16)
    chunk = data.tobytes()
    
    zcr = calculate_zcr(chunk)
    # ZCR for a sine wave is 2*f/fs. For 100Hz at 44.1kHz, it's ~0.0045
    assert zcr < 0.05

def test_calculate_zcr_noise_high():
    # High frequency white noise
    data = np.random.uniform(-10000, 10000, 1024).astype(np.int16)
    chunk = data.tobytes()
    
    zcr = calculate_zcr(chunk)
    # White noise has very high ZCR, typically > 0.3
    assert zcr > 0.2

def test_calculate_zcr_empty():
    assert calculate_zcr(b'') == 0.0
