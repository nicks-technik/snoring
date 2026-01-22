# Track Specification: LINE Messaging API Integration

## Overview
This track implements a third intervention method for snoring detection: sending a notification message via the LINE Messaging API. This provides users with an alternative to Telegram and Fritz!Box calls, allowing for flexible alerting configurations.

## Functional Requirements
1.  **LINE Connectivity:** The application must securely connect to the LINE Messaging API using the official `line-bot-sdk`.
2.  **Messaging:** Upon a snoring detection event, the application must send a text alert to a specified LINE User ID.
3.  **Configurable Connection:** LINE Channel Access Token, Channel Secret, and target User ID must be configurable via environment variables.
4.  **Coexistence:** The LINE notifier must be able to operate simultaneously with Telegram and Fritz!Box notifiers if their respective configurations are present.
5.  **Explicit Toggle:** A `LINE_ENABLED` environment variable will be used to explicitly enable or disable the LINE intervention.

## Technical Details
- **Library:** `line-bot-sdk` will be added to the project dependencies.
- **Implementation:** A new `LineNotifier` class will be created in `snoring/line_notifier.py`.
- **Sync/Async:** The `send_alert` method will be implemented synchronously (initially) as per user preference, but wrapped or called within the async detection loop.
- **Environment Variables:**
    - `LINE_ENABLED` (True/False)
    - `LINE_CHANNEL_ACCESS_TOKEN`
    - `LINE_CHANNEL_SECRET`
    - `LINE_USER_ID`

## Acceptance Criteria
- [ ] Successfully authenticates with the LINE Messaging API.
- [ ] Correctly sends a text message when a snoring event occurs and LINE is enabled.
- [ ] Environment variables are correctly loaded and respected.
- [ ] Does not interfere with Telegram or Fritz!Box notifiers.
- [ ] Handles API errors gracefully without crashing the main loop.

## Out of Scope
- Support for LINE Stickers, images, or rich menus.
- Handling incoming LINE messages (Webhooks).