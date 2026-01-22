# Track Specification: Include Metrics in Alerts

## Overview
This track updates the notification messages sent by the application (via Telegram, LINE, etc.) to include key detection metrics. Specifically, it will include the RMS (Root Mean Square) value and the ZCR (Zero-Crossing Rate) to provide more context about the detected event.

## Functional Requirements
1.  **Updated Alert Message:** The alert message text must be updated to include the RMS value of the detected audio chunk.
2.  **Concise Format:** The message should follow the format: `"Snoring detected! (RMS: <value>, ZCR: <value>)"`.
3.  **Consistency:** This change should apply to all active notifiers (Telegram, LINE).
4.  **Logging:** Ensure log messages reflect this detailed information as well.

## Technical Details
- **Module:** Update `snoring/detector.py`.
- **Change:** Modify the `step_async` method where the alert is triggered.
- **Values:** Pass the calculated `rms` and `zcr` variables into the message string.

## Acceptance Criteria
- [ ] Telegram messages contain the RMS and ZCR values.
- [ ] LINE messages contain the RMS and ZCR values.
- [ ] Unit tests are updated to verify the new message format.