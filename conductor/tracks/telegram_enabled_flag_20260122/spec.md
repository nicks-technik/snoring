# Specification: Add Telegram Enabled Flag

## Overview
Currently, the application initializes the Telegram notifier automatically if the credentials are found in the environment. This track introduces a `TELEGRAM_ENABLED` environment variable to provide explicit control, consistent with other notifiers.

## Functional Requirements
1.  **Explicit Toggle:** The application must check for a `TELEGRAM_ENABLED` environment variable.
2.  **Conditional Initialization:** The `TelegramNotifier` should only be initialized if `TELEGRAM_ENABLED` is `true`.
3.  **Default Behavior:** If `TELEGRAM_ENABLED` is missing, it should default to `false`.
4.  **Error Handling:** If `TELEGRAM_ENABLED` is `true` but credentials are missing, it should log an error and skip the notifier.

## Technical Details
- **Environment Variables:**
    - `TELEGRAM_ENABLED` (True/False)
- **Modifications:**
    - Update `snoring/cli.py` to read `TELEGRAM_ENABLED`.
    - Update `.env.example`.

## Acceptance Criteria
- [ ] `TelegramNotifier` is not initialized if `TELEGRAM_ENABLED` is `False`.
- [ ] `TelegramNotifier` is initialized if `TELEGRAM_ENABLED` is `True`.
- [ ] `.env.example` contains the new flag.
