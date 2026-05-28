# Track Specification: X.com (Twitter) DM Integration

## Overview
This track implements a fourth intervention method for snoring detection: sending a private Direct Message (DM) via X.com (Twitter). This adds another layer of redundancy and platform choice for the user.

## Functional Requirements
1.  **X.com Connectivity:** The application must securely connect to the X.com API v2 using the `tweepy` library.
2.  **Direct Messaging:** Upon a snoring detection event, the application must send a text alert as a DM to a specified recipient User ID.
3.  **Configurable Connection:** All required OAuth 1.0a credentials (API Key, API Secret, Access Token, Access Secret) and the recipient ID must be configurable via environment variables.
4.  **Explicit Toggle:** An `X_ENABLED` environment variable will be used to explicitly enable or disable the X.com intervention.
5.  **Graceful Error Handling:** If the X.com API call fails (e.g., due to rate limits or network issues), the application should log a warning but continue with other configured notifiers.

## Technical Details
- **Library:** `tweepy` will be added to the project dependencies.
- **Implementation:** A new `XNotifier` class will be created in `snoring/x_notifier.py`.
- **Sync/Async:** Consistent with recent additions, `send_alert` will be synchronous but called within the async detection loop.
- **Environment Variables:**
    - `X_ENABLED` (True/False)
    - `X_API_KEY`
    - `X_API_SECRET`
    - `X_ACCESS_TOKEN`
    - `X_ACCESS_SECRET`
    - `X_RECIPIENT_ID` (Numeric ID of the account to receive DMs)

## Acceptance Criteria
- [ ] Successfully authenticates with X.com via `tweepy`.
- [ ] Correctly sends a DM when a snoring event occurs and X is enabled.
- [ ] Environment variables are correctly loaded and respected.
- [ ] Handles rate limit errors without crashing the main loop.
- [ ] Operates correctly alongside Telegram, LINE, and Fritz!Box notifiers.

## Out of Scope
- Public tweets or media uploads.
- Managing DM conversations (reading messages).
- Handling OAuth login flow (tokens must be provided manually in `.env`).