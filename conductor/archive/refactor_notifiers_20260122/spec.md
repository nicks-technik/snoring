# Specification: Refactor Notifiers

## Problem
The file `snoring/notifier.py` contains the `TelegramNotifier` class. This naming is inconsistent with other notifiers (`fritz_notifier.py`, `line_notifier.py`, `x_notifier.py`) and vague.

## Solution
1.  Rename `snoring/notifier.py` to `snoring/telegram_notifier.py`.
2.  Update all imports in the codebase that reference `snoring.notifier`.
    - `snoring/cli.py`
    - `tests/test_notifier.py` (Rename to `tests/test_telegram_notifier.py` as well?) -> Yes, `tests/test_telegram_notifier.py` is better.
    - Check other files for imports.

## Technical Details
- Move file `snoring/notifier.py` -> `snoring/telegram_notifier.py`.
- Move file `tests/test_notifier.py` -> `tests/test_telegram_notifier.py`.
- Search and replace `from snoring.notifier` to `from snoring.telegram_notifier`.

## Testing
- Run tests to ensure imports are correct and functionality is preserved.
