# Implementation Plan - X.com Pivot to Tweets and Detector Bug Fix

## Phase 1: Detector Logic & Notification Order [checkpoint: ede9c9d]
- [x] Task: Ensure SnoreDetector handles sync/async notifiers
    - [x] Verify `snoring/detector.py` uses `asyncio.iscoroutine` to safely await notifiers.
    - [x] Update `tests/test_detector.py` with a specific test case for a mix of sync and async notifiers.
- [x] Task: Verify Notifier Priority
    - [x] Ensure `snoring/cli.py` instantiates `XNotifier` before `FritzNotifier`.
    - [x] Update integration tests to verify the order of notifiers in the `SnoreDetector` list.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Detector Logic & Notification Order' (Protocol in workflow.md) ede9c9d

## Phase 2: XNotifier Pivot to Tweet Mode
- [x] Task: Implement Tweet-based alerting in XNotifier c2dd896
    - [x] Modify `snoring/x_notifier.py` to use `self.client.create_tweet(text=message)` instead of DM methods.
    - [x] Add a unique timestamp (e.g., using `datetime.now().strftime('%H:%M:%S')`) to each message string to prevent X.com duplicate tweet errors.
- [x] Task: Update XNotifier tests c2dd896
    - [x] Modify `tests/test_x_notifier.py` to assert that `create_tweet` is called with the expected metrics and timestamp.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: XNotifier Pivot to Tweet Mode' (Protocol in workflow.md)

## Phase 3: Final Integration & Cleanup
- [ ] Task: Final project-wide test run
    - [ ] Execute the full test suite: `$env:PYTHONPATH = "."; uv run pytest --cov=snoring`.
    - [ ] Ensure all notification channels (Telegram, LINE, Fritz, X) work correctly in the main loop.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Integration & Cleanup' (Protocol in workflow.md)
