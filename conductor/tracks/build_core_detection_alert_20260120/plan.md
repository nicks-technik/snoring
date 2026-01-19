# Implementation Plan - Build Core Snoring Detection & Alert System

## Phase 1: Environment & Project Structure [checkpoint: 4cafed0]
- [x] Task: Initialize Project with uv d9f030b
    - [x] Initialize a new Python project using `uv init`.
    - [x] Create a virtual environment and activate it.
    - [x] Add `pyaudio`, `numpy`, `python-telegram-bot`, and `python-dotenv` as dependencies using `uv add`.
    - [x] Create a `.env.example` file for configuration templates (Telegram Token, Chat ID, Sensitivity).
- [x] Task: Conductor - User Manual Verification 'Phase 1: Environment & Project Structure' (Protocol in workflow.md) a24fef1

## Phase 2: Core Audio Capture & Analysis
- [ ] Task: Implement Audio Capture Class
    - [ ] Create a `AudioRecorder` class that wraps `PyAudio` stream initialization.
    - [ ] Implement a method to read chunks of audio data.
    - [ ] Write a unit test to verify the stream opens and closes correctly (mocking PyAudio).
- [ ] Task: Implement RMS Analysis
    - [ ] Create a utility function `calculate_rms(audio_chunk)` using `numpy`.
    - [ ] Write unit tests with known byte arrays to verify RMS calculation accuracy.
- [ ] Task: Create Main Monitoring Loop
    - [ ] Create a `SnoreDetector` class that orchestrates the recorder and analysis.
    - [ ] Implement the logic: Read Chunk -> Calculate RMS -> Compare with Threshold.
    - [ ] Add logging to output current RMS values for debugging/calibration.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Core Audio Capture & Analysis' (Protocol in workflow.md)

## Phase 3: Alerting & Integration
- [ ] Task: Implement Telegram Notifier
    - [ ] Create a `TelegramNotifier` class using `python-telegram-bot`.
    - [ ] Implement an asynchronous method `send_alert(message)`.
    - [ ] Write an integration test (or manual script) to verify a test message can be sent.
- [ ] Task: Integrate Alerting with Detection
    - [ ] Update `SnoreDetector` to trigger `TelegramNotifier.send_alert` when the threshold is breached.
    - [ ] Add a cooldown mechanism to prevent spamming messages (e.g., only one alert per minute).
- [ ] Task: Finalize CLI Entry Point
    - [ ] Create `main.py` (or `__main__.py`) to load env vars, instantiate classes, and start the loop.
    - [ ] Ensure `KeyboardInterrupt` (Ctrl+C) gracefully shuts down the stream and bot.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Alerting & Integration' (Protocol in workflow.md)
