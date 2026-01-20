# Implementation Plan - X.com (Twitter) DM Integration

## Phase 1: Dependency & Configuration [checkpoint: a7da86c]
- [x] Task: Add tweepy dependency b7b93b4
    - [ ] Run `uv add tweepy` to install the library.
    - [ ] Update `tech-stack.md` to include `tweepy`.
- [x] Task: Update Configuration Logic d8bdcef
    - [ ] Update `.env.example` with `X_ENABLED`, `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET`, and `X_RECIPIENT_ID`.
    - [ ] Update `snoring/cli.py` to load these new environment variables.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md) a7da86c

## Phase 2: XNotifier Implementation [checkpoint: 995b928]
- [x] Task: Implement XNotifier Class 5a5ad76
    - [ ] Create `snoring/x_notifier.py`.
    - [ ] Implement `__init__` to initialize the `tweepy.Client`.
    - [ ] Implement `send_alert()` method using the `create_direct_message` API.
    - [ ] Write unit tests mocking `tweepy` to verify DM delivery and error handling.
- [x] Task: Conductor - User Manual Verification 'Phase 2: XNotifier Implementation' (Protocol in workflow.md) 995b928

## Phase 3: Integration & Orchestration
- [x] Task: Wire up X.com in CLI a990e8f
    - [ ] Update `snoring/cli.py` to instantiate `XNotifier` if `X_ENABLED` is set to True.
    - [ ] Add the `XNotifier` instance to the list of notifiers passed to the `SnoreDetector`.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Integration & Orchestration' (Protocol in workflow.md)