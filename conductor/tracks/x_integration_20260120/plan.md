# Implementation Plan - X.com (Twitter) DM Integration

## Phase 1: Dependency & Configuration
- [ ] Task: Add tweepy dependency
    - [ ] Run `uv add tweepy` to install the library.
    - [ ] Update `tech-stack.md` to include `tweepy`.
- [ ] Task: Update Configuration Logic
    - [ ] Update `.env.example` with `X_ENABLED`, `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET`, and `X_RECIPIENT_ID`.
    - [ ] Update `snoring/cli.py` to load these new environment variables.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md)

## Phase 2: XNotifier Implementation
- [ ] Task: Implement XNotifier Class
    - [ ] Create `snoring/x_notifier.py`.
    - [ ] Implement `__init__` to initialize the `tweepy.Client`.
    - [ ] Implement `send_alert()` method using the `create_direct_message` API.
    - [ ] Write unit tests mocking `tweepy` to verify DM delivery and error handling.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: XNotifier Implementation' (Protocol in workflow.md)

## Phase 3: Integration & Orchestration
- [ ] Task: Wire up X.com in CLI
    - [ ] Update `snoring/cli.py` to instantiate `XNotifier` if `X_ENABLED` is set to True.
    - [ ] Add the `XNotifier` instance to the list of notifiers passed to the `SnoreDetector`.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Integration & Orchestration' (Protocol in workflow.md)