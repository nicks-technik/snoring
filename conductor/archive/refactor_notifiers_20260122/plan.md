# Implementation Plan

1.  [x] **Rename Files**:
    *   Rename `snoring/notifier.py` to `snoring/telegram_notifier.py`.
    *   Rename `tests/test_notifier.py` to `tests/test_telegram_notifier.py`.
2.  [x] **Update Imports**:
    *   Update `snoring/cli.py`.
    *   Update `tests/test_telegram_notifier.py` (imports inside the test).
    *   Update `tests/test_cli.py` (if it imports it).
    *   Check any other files using `grep`.
3.  [x] **Verification**: Run all tests to confirm the refactor is successful. [N/A]
