# Implementation Plan - Include Metrics in Alerts

## Phase 1: Detector Logic Update
- [x] Task: Update SnoreDetector alert message construction 941aaa3
    - [ ] Modify `snoring/detector.py`'s `step_async` method to include the `rms` and `zcr` values in the message sent to notifiers.
    - [ ] Format the values to 2 decimal places for RMS and 4 decimal places for ZCR.
    - [ ] Update unit tests in `tests/test_detector_zcr.py` to verify that the notifiers are called with the detailed message string.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Detector Logic Update' (Protocol in workflow.md)