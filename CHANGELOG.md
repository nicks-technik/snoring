# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-01-20

### Added
- **Core Snoring Detection:** Real-time RMS-based audio analysis to detect snoring.
- **Telegram Alerts:** Instant notifications sent to a configured Telegram chat.
- **Configurable Sensitivity:** `SENSITIVITY_THRESHOLD` setting to adjust detection levels.
- **Smart Cooldown:** `INTERVAL_SECONDS` setting to prevent alert spamming (default 60s).
- **CLI Interface:** Simple command-line entry point with logging.
- **Environment Management:** Project structure managed by `uv` with `.env` configuration.
