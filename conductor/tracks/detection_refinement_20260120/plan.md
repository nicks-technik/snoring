# Implementation Plan - Improved Snoring Detection Algorithm

## Phase 1: Dependency & Configuration [checkpoint: aff0754]
- [x] Task: Add librosa dependency 2fee586
    - [ ] Run `uv add librosa` to install the library.
    - [ ] Update `tech-stack.md` to include `librosa`.
- [x] Task: Update Configuration Logic 2fec477
    - [ ] Update `.env.example` with `ZCR_THRESHOLD` (e.g., default 0.1).
    - [ ] Update `snoring/cli.py` to load and parse the `ZCR_THRESHOLD` environment variable.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md) aff0754

## Phase 2: Audio Utilities Enhancement [checkpoint: d5b4715]
- [x] Task: Implement ZCR Calculation 680c4a5
    - [ ] Update `snoring/audio_utils.py` to include a `calculate_zcr` function using `librosa`.
    - [ ] Write unit tests in `tests/test_audio_utils.py` to verify ZCR calculation for different simulated waveforms (e.g., low-frequency sine vs. high-frequency noise).
- [x] Task: Conductor - User Manual Verification 'Phase 2: Audio Utilities Enhancement' (Protocol in workflow.md) d5b4715

## Phase 3: Detector Refinement
- [ ] Task: Update SnoreDetector Logic
    - [ ] Refactor `SnoreDetector.step_async` in `snoring/detector.py` to incorporate the ZCR check.
    - [ ] Update `__init__` to accept `zcr_threshold`.
    - [ ] Ensure logging includes both RMS and ZCR values during detection.
    - [ ] Write unit tests in `tests/test_detector.py` mocking `calculate_zcr` to verify the multi-stage detection logic.
- [ ] Task: Wire up ZCR in CLI
    - [ ] Update `snoring/cli.py` to pass the loaded `zcr_threshold` to the `SnoreDetector` instance.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Detector Refinement' (Protocol in workflow.md)