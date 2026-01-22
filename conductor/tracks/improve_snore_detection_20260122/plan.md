# Implementation Plan

1.  [x] **Audio Utils**: Implement `calculate_spectral_centroid` in `snoring/audio_utils.py`. [fd23e6d]
2.  [x] **Audio Utils Tests**: Add unit tests for the new function in `tests/test_audio_utils_centroid.py`. [fd23e6d]
3.  [x] **Detector Update**: Modify `SnoreDetector` in `snoring/detector.py` to:
    *   Accept `spectral_centroid_threshold` and `min_consecutive_chunks`.
    *   Integrate spectral centroid check.
    *   Implement consecutive chunk logic. [c5bbbde]
4.  [x] **Detector Tests**: Update `tests/test_detector.py` to cover new logic (centroid filtering + consecutive chunks). [c5bbbde]
5.  [x] **CLI/Main Update**: Update `main.py` (and `cli.py` arguments) to pass `sample_rate` to detector (needed for centroid) and expose new parameters. [8bd28f1]
6.  [ ] **Verification**: Run all tests to ensure no regression and verify improvement.
