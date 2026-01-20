# Implementation Plan - Fritz!Box Internal Call Integration

## Phase 1: Dependency & Configuration [checkpoint: 2d199c1]
- [x] Task: Add fritzconnection dependency 6dae759
    - [ ] Run `uv add fritzconnection` to install the library.
    - [ ] Update `tech-stack.md` to include `fritzconnection`.
- [x] Task: Update Configuration Logic c39be8a
    - [ ] Update `.env.example` with `FRITZ_ADDRESS`, `FRITZ_USER`, `FRITZ_PASSWORD`, `FRITZ_TARGET_NUMBER`, and `FRITZ_RING_DURATION`.
    - [ ] Update `snoring/cli.py` to load these new environment variables.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Dependency & Configuration' (Protocol in workflow.md) 2d199c1

## Phase 2: FritzNotifier Implementation [checkpoint: c64bfe2]
- [x] Task: Implement FritzNotifier Class de0fe3d
    - [ ] Create `snoring/fritz_notifier.py`.
    - [ ] Implement `__init__` to establish connection using `FritzConnection`.
    - [ ] Implement `send_alert()` method which calls `X_AVM-DE_DialNumber`, waits `FRITZ_RING_DURATION`, and calls `X_AVM-DE_HangUp`.
    - [ ] Write unit tests mocking `FritzConnection` to verify dial and hangup sequences.
- [x] Task: Conductor - User Manual Verification 'Phase 2: FritzNotifier Implementation' (Protocol in workflow.md) c64bfe2

## Phase 3: Integration & Orchestration [checkpoint: ce57ec4]
- [x] Task: Update SnoreDetector 49834b6
    - [ ] Refactor `SnoreDetector` to accept a list of notifiers.
    - [ ] Ensure `step_async` triggers all configured notifiers.
- [x] Task: Wire up in CLI d514101
    - [ ] Update `snoring/cli.py` to instantiate `FritzNotifier` if config is present.
    - [ ] Pass the list of notifiers to the detector.
- [x] Task: Conductor - User Manual Verification 'Phase 3: Integration & Orchestration' (Protocol in workflow.md) ce57ec4
