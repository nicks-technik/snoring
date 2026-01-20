# Track Specification: Fritz!Box Internal Call Integration

## Overview
This track implements a secondary intervention method for snoring detection: triggering an internal phone call via an AVM Fritz!Box. This call serves to vibrate the user's smartwatch (linked via the VeryFit app) to gently nudge them to stop snoring.

## Functional Requirements
1.  **Fritz!Box Connectivity:** The application must securely connect to a local Fritz!Box using the TR-064 protocol.
2.  **Internal Dialing:** Upon a snoring detection event, the application must initiate an internal call to a specified internal number (e.g., `**610`).
3.  **Automatic Hangup:** The application must automatically hang up the call after a configurable duration (`FRITZ_RING_DURATION`).
4.  **Configurable Connection:** Fritz!Box IP, username, password, target internal number, and ring duration must be configurable via environment variables.
5.  **Error Handling:** The application should log a warning if the Fritz!Box is unreachable but continue monitoring and sending Telegram alerts.

## Technical Details
- **Library:** `fritzconnection` will be used to handle the TR-064 communication.
- **Service/Action:** We will use the `X_VoIP:1` service and the `X_AVM-DE_DialNumber` action for dialing, and `X_AVM-DE_HangUp` for ending the call.
- **Integration:** The `SnoreDetector` will be updated to handle multiple notifiers or a new `FritzNotifier` will be added to the orchestration.

## Acceptance Criteria
- [ ] Successfully authenticates with the Fritz!Box.
- [ ] Correctly initiates an internal call when a detection event occurs.
- [ ] Automatically hangs up after the specified duration.
- [ ] Environment variables for Fritz!Box are correctly loaded from `.env`.
- [ ] Does not crash the main monitoring loop if the call fails.

## Out of Scope
- External calls to mobile numbers via landline.
