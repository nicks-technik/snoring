# Snoring Detector CLI

A Python CLI application to detect snoring in real-time and trigger automated interventions via various platforms.

## Overview
This application monitors audio from your default input device to identify snoring patterns. It uses a multi-stage detection algorithm combining volume intensity (RMS) and frequency analysis (Zero-Crossing Rate) to minimize false positives from speech or coughing. When snoring is confirmed, it triggers configured notifiers to gently nudge the user (e.g., via smartwatch vibration).

## Features
- **Multi-Stage Detection:**
  - **Intensity (RMS):** Initial detection based on sound volume.
  - **Frequency (ZCR):** Filters out high-frequency sounds like human speech using Zero-Crossing Rate analysis.
- **Multiple Notification Channels:**
  - **Telegram:** Instant messages with detection metrics.
  - **Fritz!Box:** Triggers internal calls to vibrate connected smartwatches/phones.
  - **LINE:** Notifications via the LINE Messaging API.
- **Detailed Alerts:** Alert messages include real-time metrics (RMS and ZCR) for monitoring.
- **Configurable & Flexible:**
  - Independent toggles for each intervention method.
  - Adjustable sensitivity and frequency thresholds.
  - Smart cooldown to prevent alert fatigue.

## Prerequisites
- **Python 3.11+** (Note: Compatibility with `numba` requires Python < 3.12 for some environments, Python 3.11 is recommended).
- **PortAudio Development Headers:**
  - Debian/Ubuntu: `sudo apt-get install portaudio19-dev`
  - macOS: `brew install portaudio`
  - Windows: Typically included with PyAudio wheels.
- **Service Credentials:**
  - **Telegram:** Bot token and Chat ID from [@BotFather](https://t.me/botfather).
  - **Fritz!Box:** Local IP, TR-064 enabled user, and target internal number.
  - **LINE:** Channel Access Token, Secret, and User ID from the LINE Developers Console.

## Installation
1. Clone the repository.
2. Ensure [uv](https://github.com/astral-sh/uv) is installed.
3. Install dependencies and set up the virtual environment:
   ```bash
   uv sync
   ```

## Configuration
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and configure your settings:
   ```ini
   # Core Detection
   SENSITIVITY_THRESHOLD=500.0
   ZCR_THRESHOLD=0.1
   INTERVAL_SECONDS=60

   # Telegram
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id

   # Fritz!Box
   FRITZ_ENABLED=False
   FRITZ_ADDRESS=192.168.178.1
   FRITZ_USER=your_username
   FRITZ_PASSWORD=your_password
   FRITZ_TARGET_NUMBER=**610
   FRITZ_RING_DURATION=20

   # LINE
   LINE_ENABLED=False
   LINE_CHANNEL_ACCESS_TOKEN=your_token
   LINE_CHANNEL_SECRET=your_secret
   LINE_USER_ID=your_user_id
   ```

## Usage
Run the application using `uv`:
```bash
uv run snoring
```
Alternatively, if the virtual environment is activated:
```bash
snoring
```
Or run the script directly:
```bash
uv run python main.py
```

## Testing
Run the automated test suite with coverage:
```bash
$env:PYTHONPATH = "."; uv run pytest --cov=snoring
```

## Contributing
1.  Fork the repository.
2.  Create a feature branch: `git checkout -b feature/your-feature`.
3.  Implement your changes following the [Project Workflow](./conductor/workflow.md).
4.  Ensure all tests pass and coverage is maintained.
5.  Submit a pull request.

## Project Structure
- `snoring/`: Core application logic.
  - `audio_recorder.py`: Audio capture using PyAudio.
  - `audio_utils.py`: Numerical analysis (RMS, ZCR) using NumPy and Librosa.
  - `detector.py`: Detection orchestration and notifier management.
  - `notifier.py`: Telegram integration.
  - `fritz_notifier.py`: Fritz!Box TR-064 integration.
  - `line_notifier.py`: LINE Messaging API integration.
  - `cli.py`: CLI entry point and configuration loading.
- `tests/`: Unit and integration tests.
- `conductor/`: Project management, specifications, and implementation tracks.