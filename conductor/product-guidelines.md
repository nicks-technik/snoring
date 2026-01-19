# Product Guidelines

## Prose Style & Tone
- **Professional & Functional:** Use direct, objective language. The focus is on utility and reliability.
- **Concise:** Avoid fluff. Log messages and status updates should be brief and actionable.
- **Technical Accuracy:** Ensure technical terms are used correctly, especially regarding audio processing and networking.

## CLI Visual Identity
- **Minimalist Design:** Maintain a clean interface. Avoid excessive output that could clutter the terminal during overnight runs.
- **Clear Status Indicators:** Use consistent prefixes for different types of messages:
    - `[INFO]` for general status (e.g., "Monitoring started").
    - `[DETECT]` for snoring events.
    - `[WARN]` for potential issues (e.g., "High ambient noise").
    - `[ERROR]` for critical failures.
- **Optional Visual Feedback:** If requested, use simple ASCII-based level meters to help users calibrate sensitivity without needing a complex GUI.

## Interaction Principles
- **One-Command Operation:** Users should be able to start monitoring with a single command and minimal required arguments.
- **Easy Calibration:** The process of adjusting sensitivity should be intuitive, providing immediate feedback on whether current sound levels exceed the set threshold.
- **Reliable Alerts:** The Telegram notification should be formatted clearly, containing the timestamp and a brief confirmation of the event.

## User Feedback & Error Handling
- **Graceful Failures:** If a Telegram message fails to send, the CLI should log the error and continue monitoring rather than crashing.
- **Explicit Setup:** Guide the user clearly through the initial configuration (e.g., setting up the Telegram Bot API key and sensitivity levels).
