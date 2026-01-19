# Track Specification: Build Core Snoring Detection & Alert System

## Overview
This track focuses on building the foundational elements of the snoring detection CLI. It involves setting up the Python environment using `uv`, implementing real-time audio capture and analysis, and creating the alerting mechanism via Telegram.

## Goals
1.  **Project Setup:** Initialize a robust Python project structure managed by `uv`.
2.  **Audio Capture:** Implement reliable, real-time audio recording using `PyAudio`.
3.  **Snoring Detection:** develop a basic RMS-based algorithm to detect snoring events based on sound intensity.
4.  **Alerting:** Integrate `python-telegram-bot` to send notifications to the user upon detection.
5.  **Configuration:** Enable sensitivity and API token configuration via environment variables.

## Key Features
-   **CLI Interface:** A simple command-line entry point to start the application.
-   **Audio Monitoring:** Continuous loop reading from the default microphone.
-   **RMS Calculation:** Real-time computation of audio buffer intensity.
-   **Threshold Logic:** Configurable threshold to trigger an "event".
-   **Telegram Notification:** Asynchronous message sending to a specified chat.

## Non-Functional Requirements
-   **Latency:** Audio processing should happen in near real-time.
-   **Stability:** The application should run overnight without crashing on network hiccups (e.g., Telegram API timeouts).
-   **Privacy:** No audio data should be saved to disk or uploaded.

## Dependencies
-   `uv` (Package Manager)
-   `PyAudio`
-   `NumPy`
-   `python-telegram-bot`
-   `python-dotenv` (for loading .env files)
