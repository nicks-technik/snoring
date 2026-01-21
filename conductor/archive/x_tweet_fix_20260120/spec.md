# Track Specification: Refine X.com Integration and Fix Detector Bug

## Overview
This track addresses the limitations of the X.com Free Tier by switching from Direct Messages to public Tweets (intended for use with a private/protected account). It also fixes a critical bug in the `SnoreDetector` related to awaiting synchronous notifiers and reorders the notification chain to prioritize X.com alerts.

## Functional Requirements
1.  **Switch to Tweets:** The `XNotifier` must be updated to use `client.create_tweet()` instead of Direct Message endpoints.
2.  **Unique Tweet Content:** To avoid X.com's duplicate tweet prevention, each alert must include a timestamp or unique identifier alongside the RMS and ZCR metrics.
3.  **Fix Await Bug:** Update `SnoreDetector.step_async` to safely handle both synchronous and asynchronous notifiers, preventing the `NoneType can't be used in 'await' expression` error.
4.  **Prioritize X.com:** Reorder the notification sequence in `snoring/cli.py` to ensure X.com alerts are triggered before the Fritz!Box internal call.

## Technical Details
- **Module:** `snoring/x_notifier.py` - Update `send_alert` to use `create_tweet`.
- **Module:** `snoring/detector.py` - Implement a check for coroutines before awaiting notifier results.
- **Module:** `snoring/cli.py` - Reorder the instantiation and list-building of notifiers.

## Acceptance Criteria
- [ ] Successfully posts a tweet upon snoring detection (verified via logs or X.com).
- [ ] Alert message in the tweet includes RMS, ZCR, and a unique timestamp.
- [ ] The application no longer crashes with a `TypeError` when triggering notifiers.
- [ ] X.com notifications are logged/triggered before Fritz!Box calls.
- [ ] Unit tests are updated to reflect the switch to Tweets and the fix for the await logic.
