# Changelog

All notable changes to this project will be documented in this file.

## [0.1.6] - 2026-01-21

### Changed
- **X.com Pivot:** Switched from Direct Messages to public Tweets (optimized for protected accounts) to support the X.com API Free Tier.
- **Priority Alerts:** Reordered notification sequence to trigger X.com alerts before other methods.

### Fixed
- **Detector Reliability:** Fixed a `TypeError` when triggering synchronous notifiers within the async monitoring loop.

## [0.1.5] - 2026-01-20

### Added
- **X.com Integration:** Support for sending Direct Messages via the X.com (Twitter) API v2.
- **Configurable Notifiers:** Added `X_ENABLED` toggle.

### Fixed
- **Fritz!Box Compatibility:** Corrected service and action names for improved hardware compatibility.
- **Detector Reliability:** Fixed a bug that allowed overlapping alert triggers during notification processing.
- **Project Structure:** Added `snoring.egg-info/` to `.gitignore`.

## [0.1.4] - 2026-01-20

### Added
- **Detailed Alerts:** Notification messages (Telegram, LINE) now include detection metrics: RMS (intensity) and ZCR (frequency).
- **ZCR Filtering:** Improved snoring detection algorithm using Zero-Crossing Rate to filter out high-frequency false positives like speech and coughing.
- **Git Maintenance:** Added `.coverage` to `.gitignore` and removed it from the repository.

## [0.1.3] - 2026-01-20

### Added
- **LINE Integration:** Added support for sending alerts via the LINE Messaging API.
- **Explicit Notifier Control:** Added `FRITZ_ENABLED` and `LINE_ENABLED` environment variables to explicitly toggle intervention methods.
- **Improved Orchestration:** Enhanced `SnoreDetector` to handle a dynamic list of notifiers.

## [0.1.1] - 2026-01-20

### Added
- **Fritz!Box Integration:** Support for triggering internal calls on a local Fritz!Box to vibrate connected devices (e.g., smartwatches).
- **Dual Alerting:** SnoreDetector now supports multiple simultaneous notifiers (Telegram + Fritz!Box).
- **Configuration:** New environment variables `FRITZ_ADDRESS`, `FRITZ_USER`, `FRITZ_PASSWORD`, `FRITZ_TARGET_NUMBER`, and `FRITZ_RING_DURATION`.

## [0.1.0] - 2026-01-20

### Added
- **Core Snoring Detection:** Real-time RMS-based audio analysis to detect snoring.
- **Telegram Alerts:** Instant notifications sent to a configured Telegram chat.
- **Configurable Sensitivity:** `SENSITIVITY_THRESHOLD` setting to adjust detection levels.
- **Smart Cooldown:** `INTERVAL_SECONDS` setting to prevent alert spamming (default 60s).
- **CLI Interface:** Simple command-line entry point with logging.
- **Environment Management:** Project structure managed by `uv` with `.env` configuration.
