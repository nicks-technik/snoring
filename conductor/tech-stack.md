# Tech Stack

## Programming Language
- **Python 3.12+:** Leveraged for its rich ecosystem of audio processing and networking libraries.

## Package & Environment Management
- **uv:** A high-performance Python package manager and project tool. All dependencies and virtual environments will be managed through `uv`.

## Core Libraries
- **PyAudio:** Provides cross-platform audio recording capabilities.
- **NumPy:** Used for efficient, real-time numerical analysis of audio buffers.
- **python-telegram-bot:** Handles integration with the Telegram Bot API for sending intervention alerts.
- **fritzconnection:** Interfaces with AVM Fritz!Box for triggering internal calls via TR-064.
- **line-bot-sdk:** Official SDK for the LINE Messaging API to send notifications.
- **Librosa:** Used for advanced audio analysis (Zero-Crossing Rate) to reduce false positives.
- **tweepy:** Interfaces with X.com (Twitter) API v2 for sending Direct Messages.

## Configuration & Secrets
- **Environment Variables (.env):** Used to store sensitive configuration like the Telegram Bot Token and Chat ID.
- **Project Structure:** Standard Python project layout managed by `uv`, including `pyproject.toml`.

## Audio Processing Strategy
- **Buffer-Based Analysis:** Real-time processing of incoming audio streams using NumPy for calculations like RMS (Root Mean Square) to detect intensity peaks.
- **Multi-Stage Detection:** Employs RMS (intensity), Zero-Crossing Rate (frequency), and Spectral Centroid analysis to accurately identify snoring. It also verifies consecutive frames to ensure sustained sound, filtering out transient noises and speech.

