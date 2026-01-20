# Implementation Plan - Improved Snoring Detection Algorithm

## Phase 1: Dependency & Configuration
- [x] Task: Add librosa dependency 2fee586
    - [ ] Run `uv add librosa` to install the library.
    - [ ] Update `tech-stack.md` to include `librosa`.
- [x] Task: Update Configuration Logic 2fec477
    - [ ] Update `.env.example` with `ZCR_THRESHOLD` (e.g., default 0.1).
    - [ ] Update `snoring/cli.py` to load and parse the `ZCR_THRESHOLD` environment variable.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md)

## Phase 2: Audio Utilities Enhancement
- [ ] Task: Implement ZCR Calculation
    - [ ] Update `snoring/audio_utils.py` to include a `calculate_zcr` function using `librosa`.
    - [ ] Write unit tests in `tests/test_audio_utils.py` to verify ZCR calculation for different simulated waveforms (e.g., low-frequency sine vs. high-frequency noise).
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Audio Utilities Enhancement' (Protocol in workflow.md)

## Phase 3: Detector Refinement
- [ ] Task: Update SnoreDetector Logic
    - [ ] Refactor `SnoreDetector.step_async` in `snoring/detector.py` to incorporate the ZCR check.
    - [ ] Update `__init__` to accept `zcr_threshold`.
    - [ ] Ensure logging includes both RMS and ZCR values during detection.
    - [ ] Write unit tests in `tests/test_detector.py` mocking `calculate_zcr` to verify the multi-stage detection logic.
- [ ] Task: Wire up ZCR in CLI
    - [ ] Update `snoring/cli.py` to pass the loaded `zcr_threshold` to the `SnoreDetector` instance.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Detector Refinement' (Protocol in workflow.md)