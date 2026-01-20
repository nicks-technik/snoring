# Snoring Detector CLI

A Python CLI application to detect snoring in real-time and send alerts via Telegram.

## Features
- **Real-Time Audio Analysis:** Monitors audio from the default input device and identifies snoring patterns based on sound intensity (RMS).
- **Configurable Sensitivity:** Adjust the detection threshold via environment variables.
- **Telegram Alerts:** Sends instant notifications to a specified Telegram chat when snoring is detected.
- **Cooldown Mechanism:** Prevents spamming alerts by enforcing a minimum time interval between notifications (default: 60 seconds).
- **Lightweight & Efficient:** Uses NumPy for fast numerical processing and uv for modern dependency management.

## Prerequisites
- **Python 3.12+**
- **PortAudio Development Headers:**
  - Debian/Ubuntu: `sudo apt-get install portaudio19-dev`
  - macOS: `brew install portaudio`
- **Telegram Bot:** A bot token and your chat ID. Use [@BotFather](https://t.me/botfather) to create a bot.

## Installation
1. Clone the repository.
2. Ensure [uv](https://github.com/astral-sh/uv) is installed.
3. Install dependencies:
   ```bash
   uv sync
   ```

## Configuration
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and provide your credentials:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   SENSITIVITY_THRESHOLD=500.0
   INTERVAL_SECONDS=60
   ```

## Usage
Run the application:
```bash
uv run python main.py
```

## Testing
Run the automated test suite:
```bash
uv run env PYTHONPATH=. pytest --cov=snoring
```

## Project Structure
- `snoring/`: Core application logic.
  - `audio_recorder.py`: Audio capture using PyAudio.
  - `audio_utils.py`: Numerical analysis utilities.
  - `detector.py`: Detection orchestration and loop logic.
  - `notifier.py`: Telegram integration.
  - `cli.py`: CLI entry point.
- `tests/`: Unit and integration tests.
- `conductor/`: Project management and specification.
