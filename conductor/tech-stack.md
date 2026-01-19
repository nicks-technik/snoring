# Tech Stack

## Programming Language
- **Python 3.12+:** Leveraged for its rich ecosystem of audio processing and networking libraries.

## Package & Environment Management
- **uv:** A high-performance Python package manager and project tool. All dependencies and virtual environments will be managed through `uv`.

## Core Libraries
- **PyAudio:** Provides cross-platform audio recording capabilities.
- **NumPy:** Used for efficient, real-time numerical analysis of audio buffers.
- **python-telegram-bot:** Handles integration with the Telegram Bot API for sending intervention alerts.

## Configuration & Secrets
- **Environment Variables (.env):** Used to store sensitive configuration like the Telegram Bot Token and Chat ID.
- **Project Structure:** Standard Python project layout managed by `uv`, including `pyproject.toml`.

## Audio Processing Strategy
- **Buffer-Based Analysis:** Real-time processing of incoming audio streams using NumPy for calculations like RMS (Root Mean Square) to detect intensity peaks.
- **Threshold-Based Detection:** Initial MVP logic will use configurable intensity and duration thresholds to identify snoring events.
