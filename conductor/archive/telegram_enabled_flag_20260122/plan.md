# Implementation Plan

1.  [x] **Configuration**: Add `TELEGRAM_ENABLED=false` to `.env.example`. [1fe5a24]
2.  [x] **CLI Update**: Modify `snoring/cli.py` to respect the `TELEGRAM_ENABLED` flag. [1fe5a24]
3.  [x] **Test Update**: Add/Update tests in `tests/test_cli.py` to verify the flag logic. [1fe5a24]
4.  [x] **Verification**: Run all tests. [1fe5a24]