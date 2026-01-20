# Track Specification: Add FRITZ_ENABLED Flag

## Overview
This track adds a `FRITZ_ENABLED` environment variable to explicitly control the activation of the Fritz!Box notifier, consistent with the newly added `LINE_ENABLED` flag.

## Functional Requirements
1.  **Explicit Toggle:** The application must check for a `FRITZ_ENABLED` environment variable (True/False).
2.  **Conditional Initialization:** The `FritzNotifier` should only be initialized if `FRITZ_ENABLED` is true.
3.  **Default Behavior:** If `FRITZ_ENABLED` is missing, it should default to `False`.

## Technical Details
- **Environment Variables:**
    - `FRITZ_ENABLED` (True/False)
- **Modifications:**
    - Update `snoring/cli.py` to read `FRITZ_ENABLED`.
    - Update `.env.example`.

## Acceptance Criteria
- [ ] `FritzNotifier` is not initialized if `FRITZ_ENABLED` is not set or set to False.
- [ ] `FritzNotifier` is initialized if `FRITZ_ENABLED` is set to True (and address is valid).