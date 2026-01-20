# Implementation Plan - X.com Pivot to Tweets and Detector Bug Fix

## Phase 1: Detector Logic & Notification Order
- [ ] Task: Ensure SnoreDetector handles sync/async notifiers
    - [ ] Verify `snoring/detector.py` uses `asyncio.iscoroutine` to safely await notifiers.
    - [ ] Update `tests/test_detector.py` with a specific test case for a mix of sync and async notifiers.
- [ ] Task: Verify Notifier Priority
    - [ ] Ensure `snoring/cli.py` instantiates `XNotifier` before `FritzNotifier`.
    - [ ] Update integration tests to verify the order of notifiers in the `SnoreDetector` list.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Detector Logic & Notification Order' (Protocol in workflow.md)

## Phase 2: XNotifier Pivot to Tweet Mode
- [ ] Task: Implement Tweet-based alerting in XNotifier
    - [ ] Modify `snoring/x_notifier.py` to use `self.client.create_tweet(text=message)` instead of DM methods.
    - [ ] Add a unique timestamp (e.g., using `datetime.now().strftime('%H:%M:%S')`) to each message string to prevent X.com duplicate tweet errors.
- [ ] Task: Update XNotifier tests
    - [ ] Modify `tests/test_x_notifier.py` to assert that `create_tweet` is called with the expected metrics and timestamp.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: XNotifier Pivot to Tweet Mode' (Protocol in workflow.md)

## Phase 3: Final Integration & Cleanup
- [ ] Task: Final project-wide test run
    - [ ] Execute the full test suite: `$env:PYTHONPATH = "."; uv run pytest --cov=snoring`.
    - [ ] Ensure all notification channels (Telegram, LINE, Fritz, X) work correctly in the main loop.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Final Integration & Cleanup' (Protocol in workflow.md)
