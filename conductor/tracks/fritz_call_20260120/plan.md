# Implementation Plan - Fritz!Box Internal Call Integration

## Phase 1: Dependency & Configuration
- [x] Task: Add fritzconnection dependency 6dae759
    - [ ] Run `uv add fritzconnection` to install the library.
    - [ ] Update `tech-stack.md` to include `fritzconnection`.
- [ ] Task: Update Configuration Logic
    - [ ] Update `.env.example` with `FRITZ_ADDRESS`, `FRITZ_USER`, `FRITZ_PASSWORD`, `FRITZ_TARGET_NUMBER`, and `FRITZ_RING_DURATION`.
    - [ ] Update `snoring/cli.py` to load these new environment variables.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md)

## Phase 2: FritzNotifier Implementation
- [ ] Task: Implement FritzNotifier Class
    - [ ] Create `snoring/fritz_notifier.py`.
    - [ ] Implement `__init__` to establish connection using `FritzConnection`.
    - [ ] Implement `send_alert()` method which calls `X_AVM-DE_DialNumber`, waits `FRITZ_RING_DURATION`, and calls `X_AVM-DE_HangUp`.
    - [ ] Write unit tests mocking `FritzConnection` to verify dial and hangup sequences.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: FritzNotifier Implementation' (Protocol in workflow.md)

## Phase 3: Integration & Orchestration
- [ ] Task: Update SnoreDetector
    - [ ] Refactor `SnoreDetector` to accept a list of notifiers.
    - [ ] Ensure `step_async` triggers all configured notifiers.
- [ ] Task: Wire up in CLI
    - [ ] Update `snoring/cli.py` to instantiate `FritzNotifier` if config is present.
    - [ ] Pass the list of notifiers to the detector.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Integration & Orchestration' (Protocol in workflow.md)
