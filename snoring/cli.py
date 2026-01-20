"""CLI entry point for snoring detection."""

import os
import asyncio
import logging
from dotenv import load_dotenv
from snoring.audio_recorder import AudioRecorder
from snoring.detector import SnoreDetector
from snoring.notifier import TelegramNotifier
from snoring.fritz_notifier import FritzNotifier
from snoring.line_notifier import LineNotifier

def setup_logging():
    """Configures logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

async def run_app():
    """Main application logic."""
    setup_logging()
    load_dotenv()
    
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    threshold_str = os.getenv("SENSITIVITY_THRESHOLD", "500.0")
    try:
        threshold = float(threshold_str)
    except (ValueError, TypeError):
        threshold = 500.0
        
    interval_str = os.getenv("INTERVAL_SECONDS", "60")
    try:
        interval = int(interval_str)
    except (ValueError, TypeError):
        interval = 60

    fritz_enabled = os.getenv("FRITZ_ENABLED", "False").lower() == "true"
    fritz_address = os.getenv("FRITZ_ADDRESS")
    fritz_user = os.getenv("FRITZ_USER")
    fritz_password = os.getenv("FRITZ_PASSWORD")
    fritz_target = os.getenv("FRITZ_TARGET_NUMBER")
    fritz_duration_str = os.getenv("FRITZ_RING_DURATION", "10")
    try:
        fritz_duration = int(fritz_duration_str)
    except (ValueError, TypeError):
        fritz_duration = 10

    line_enabled = os.getenv("LINE_ENABLED", "False").lower() == "true"
    line_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    line_secret = os.getenv("LINE_CHANNEL_SECRET")
    line_user_id = os.getenv("LINE_USER_ID")
    
    if not token or not chat_id:
        logging.error("Telegram token or Chat ID not found in environment.")
        return

    recorder = None
    try:
        recorder = AudioRecorder()
        
        notifiers = []
        # Setup Telegram Notifier
        notifiers.append(TelegramNotifier(token=token, chat_id=chat_id))
        
        # Setup Fritz Notifier if enabled
        if fritz_enabled and fritz_address:
            try:
                fritz_notifier = FritzNotifier(
                    address=fritz_address,
                    user=fritz_user,
                    password=fritz_password,
                    target_number=fritz_target,
                    ring_duration=fritz_duration
                )
                notifiers.append(fritz_notifier)
                logging.info("Fritz!Box notifier enabled.")
            except Exception as e:
                logging.warning(f"Could not initialize Fritz!Box notifier: {e}")

        # Setup LINE Notifier if enabled
        if line_enabled:
            try:
                line_notifier = LineNotifier(
                    access_token=line_token,
                    channel_secret=line_secret,
                    user_id=line_user_id
                )
                notifiers.append(line_notifier)
                logging.info("LINE notifier enabled.")
            except Exception as e:
                logging.warning(f"Could not initialize LINE notifier: {e}")

        detector = SnoreDetector(
            recorder=recorder,
            threshold=threshold,
            notifier=notifiers,
            cooldown_seconds=interval
        )
        await detector.start_loop_async()
    except Exception as e:
        logging.error(f"Application error: {e}")
    finally:
        if recorder:
            recorder.close()

def main():
    """CLI entry point."""
    try:
        asyncio.run(run_app())
    except KeyboardInterrupt:
        # Handled by detector start_loop_async usually, 
        # but here as a secondary safety.
        pass

if __name__ == "__main__":
    main()
