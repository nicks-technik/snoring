# Specification: Update Documentation

## Context
The project has evolved, and the documentation has lagged behind. Specifically, `notifier.py` was renamed to `telegram_notifier.py`, `x_notifier.py` was added, and new configuration flags like `TELEGRAM_ENABLED` were introduced.

## Requirements

### `README.md` Updates
1.  **Project Structure:**
    -   Replace `notifier.py` with `telegram_notifier.py`.
    -   Add `x_notifier.py`.
2.  **Configuration Guide:**
    -   Add `TELEGRAM_ENABLED` to the Telegram configuration section.
    -   Ensure `FRITZ_ENABLED`, `LINE_ENABLED`, and `X_ENABLED` are mentioned if they aren't already explicit (they are in .env.example, but maybe not explicitly in the guide text).

## Acceptance Criteria
- [ ] `README.md` accurately lists all source files in `snoring/`.
- [ ] `README.md` documents the `TELEGRAM_ENABLED` environment variable.
