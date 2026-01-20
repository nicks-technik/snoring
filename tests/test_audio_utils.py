import numpy as np
import pytest
from snoring.audio_utils import calculate_rms

def test_calculate_rms_silence():
    chunk = b'\x00\x00' * 1024
    assert calculate_rms(chunk) == 0.0

def test_calculate_rms_known_value():
    # 16-bit PCM constant value
    val = 1000
    chunk = np.array([val] * 1024, dtype=np.int16).tobytes()
    # RMS of constant C is abs(C)
    assert calculate_rms(chunk) == pytest.approx(1000.0)

def test_calculate_rms_empty():
    assert calculate_rms(b'') == 0.0

def test_calculate_rms_invalid_size():
    # Length 1 is not multiple of 2 (int16)
    assert calculate_rms(b'\x00') == 0.0
