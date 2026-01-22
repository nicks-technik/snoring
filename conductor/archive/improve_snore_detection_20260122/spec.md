# Specification: Improve Snore Detection

## Problem
The current snoring detection algorithm yields too many false positives, especially in the presence of background noise like movies. It relies solely on RMS (volume) and Zero-Crossing Rate (ZCR).

## Solution
Enhance the detection algorithm with two additional checks:
1.  **Spectral Centroid:** Snoring generally has a lower spectral centroid (concentration of energy) compared to speech or music. We will add a threshold for this.
2.  **Temporal Consistency:** Snoring is a sustained sound, not a transient click. We will require *multiple consecutive chunks* (or a sufficient number of chunks within a window) to classification as snoring before triggering an alert.

## Technical Details

### `snoring/audio_utils.py`
- Add `calculate_spectral_centroid(audio_chunk: bytes, sample_rate: int) -> float`.
  - Use `librosa.feature.spectral_centroid` or implementing the calculation using FFT.

### `snoring/detector.py`
- Update `SnoreDetector.__init__`:
    - Add `spectral_centroid_threshold` (default e.g., 1500 Hz).
    - Add `min_consecutive_chunks` (default e.g., 3).
- Update `SnoreDetector.step` / `step_async`:
    - Calculate spectral centroid.
    - If `rms > threshold` AND `zcr < zcr_threshold` AND `centroid < centroid_threshold`:
        - Increment `consecutive_counter`.
    - Else:
        - Reset `consecutive_counter` (or decrease it for smoother handling, but reset is simpler for now).
    - Only return `True` (and trigger callbacks) if `consecutive_counter >= min_consecutive_chunks`.

### `snoring/cli.py` / `main.py`
- Update to allow configuration of these new parameters if necessary, or set reasonable defaults.

## Testing
- Unit tests for `calculate_spectral_centroid`.
- Integration tests for `SnoreDetector` verifying that single short bursts do not trigger it, but sustained "simulated" snoring does.
