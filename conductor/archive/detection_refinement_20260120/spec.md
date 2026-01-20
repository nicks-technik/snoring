# Track Specification: Improved Snoring Detection Algorithm

## Overview
This track aims to reduce false positives in snoring detection, specifically those caused by human speech or coughing. Currently, the system relies solely on an RMS (intensity) threshold. We will introduce frequency analysis using the Zero-Crossing Rate (ZCR) via the `librosa` library to distinguish between the low-frequency nature of snoring and the typically higher-frequency/more complex nature of speech.

## Functional Requirements
1.  **Librosa Integration:** Add `librosa` to the project dependencies.
2.  **Frequency Analysis (ZCR):** Implement Zero-Crossing Rate calculation for each audio chunk.
3.  **Refined Detection Logic:**
    - Perform initial RMS threshold check (existing logic).
    - If RMS > `SENSITIVITY_THRESHOLD`, perform a secondary check:
    - Only trigger an alert if the `ZCR` value is below a certain threshold (`ZCR_THRESHOLD`), as snoring is generally characterized by lower frequencies and thus lower ZCR.
4.  **Configurable Thresholds:**
    - Add `ZCR_THRESHOLD` to `.env` (default to be determined during testing, e.g., 0.1).
5.  **Logging:** Log both RMS and ZCR values for detected events to help users fine-tune their settings.

## Technical Details
- **Library:** `librosa` for audio processing (ZCR calculation).
- **Module:** Update `snoring/audio_utils.py` to include frequency analysis functions.
- **Module:** Update `snoring/detector.py` to incorporate the multi-stage detection logic.

## Acceptance Criteria
- [ ] Successfully filters out typical speech and coughing sounds that exceed the RMS threshold.
- [ ] Continues to accurately detect actual snoring events.
- [ ] `librosa` dependency is correctly managed via `uv`.
- [ ] ZCR thresholds are configurable via environment variables.
- [ ] Main loop performance remains sufficient for real-time monitoring.

## Out of Scope
- Full Spectral Centroid analysis or FFT-based pattern matching (unless ZCR proves insufficient).
- Machine Learning / Model-based classification.