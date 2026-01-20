# Implementation Plan - LINE Messaging API Integration

## Phase 1: Dependency & Configuration
- [ ] Task: Add line-bot-sdk dependency
    - [ ] Run `uv add line-bot-sdk` to install the library.
    - [ ] Update `tech-stack.md` to include `line-bot-sdk`.
- [ ] Task: Update Configuration Logic
    - [ ] Update `.env.example` with `LINE_ENABLED`, `LINE_CHANNEL_ACCESS_TOKEN`, `LINE_CHANNEL_SECRET`, and `LINE_USER_ID`.
    - [ ] Update `snoring/cli.py` to load these new environment variables.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md)

## Phase 2: LineNotifier Implementation
- [ ] Task: Implement LineNotifier Class
    - [ ] Create `snoring/line_notifier.py`.
    - [ ] Implement `__init__` to initialize the LINE API client.
    - [ ] Implement `send_alert()` method using the `push_message` functionality.
    - [ ] Write unit tests mocking the `line-bot-sdk` to verify message delivery and error handling.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: LineNotifier Implementation' (Protocol in workflow.md)

## Phase 3: Integration & Orchestration
- [ ] Task: Wire up LINE in CLI
    - [ ] Update `snoring/cli.py` to instantiate `LineNotifier` if `LINE_ENABLED` is set to True.
    - [ ] Add the `LineNotifier` instance to the list of notifiers passed to the `SnoreDetector`.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Integration & Orchestration' (Protocol in workflow.md)