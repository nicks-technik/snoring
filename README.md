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
2. Edit `.env` and configure your settings. See the [Configuration Guide](#configuration-guide) for details on where to find these values.

### Configuration Guide

#### Telegram
- **`TELEGRAM_BOT_TOKEN`**: Create a bot via [@BotFather](https://t.me/botfather) on Telegram. It will provide a token like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`.
- **`TELEGRAM_CHAT_ID`**: Send a message to your new bot, then visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` to find your `id` in the `chat` object.

#### Fritz!Box
- **`FRITZ_ADDRESS`**: Usually `192.168.178.1` or `fritz.box`.
- **`FRITZ_USER`**: A user created in **System > Fritz!Box Users**. Ensure "Telephony" rights are enabled.
- **`FRITZ_TARGET_NUMBER`**: The internal number of the device to ring (e.g., `**610`). Found in **Telephony > Telephony Devices**.
- **Note**: Ensure **Telephony > Calls > Dialing Help (Wählhilfe)** is enabled in the Fritz!Box UI.

#### LINE
- **`LINE_CHANNEL_ACCESS_TOKEN`** & **`LINE_CHANNEL_SECRET`**: Create a Messaging API channel in the [LINE Developers Console](https://developers.line.biz/console/). Tokens are in the "Messaging API" and "Basic settings" tabs.
- **`LINE_USER_ID`**: Found at the bottom of the "Messaging API" tab in the LINE Developers Console (Your user ID).

#### X.com (Twitter)
To send Direct Messages, you need an **X Developer Account**.
1.  **Set Permissions First:** In the [X Developer Portal](https://developer.x.com/), go to **App Settings > User authentication settings > Edit**. Set "App permissions" to **Read and write and Direct message** and save.
2.  **API Keys (Consumer Keys):** Go to the **Keys and Tokens** tab.
    -   **`X_API_KEY`**: This is the **Consumer Key**.
    -   **`X_API_SECRET`**: This is the **Consumer Secret** (Click "Regenerate" to see it).
3.  **User Tokens (Authentication Tokens):** In the same tab, look for **Access Token and Secret**:
    -   Click the **Generate** button next to your @username.
    -   **`X_ACCESS_TOKEN`**: Copy the provided Access Token.
    -   **`X_ACCESS_SECRET`**: Copy the provided Access Token Secret.
4.  **`X_RECIPIENT_ID`**: This is your numeric ID. It is displayed in the "Access Token and Secret" section once generated.

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