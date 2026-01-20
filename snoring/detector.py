"""Snore detector orchestration module."""

import logging
import time
import asyncio
from typing import Callable, Optional
from snoring.audio_utils import calculate_rms, calculate_zcr

logger = logging.getLogger(__name__)

class SnoreDetector:
    """Orchestrates audio recording and analysis to detect snoring."""

    def __init__(
        self,
        recorder,
        threshold: float,
        on_detection: Optional[Callable[[], None]] = None,
        notifier = None,
        cooldown_seconds: int = 60,
        zcr_threshold: float = 0.1
    ):
        """Initializes the snore detector.

        Args:
            recorder: An object with a read_chunk() method.
            threshold: The RMS threshold above which snoring is detected.
            on_detection: A callback function to execute when snoring is detected.
            notifier: A single notifier instance or a list of notifiers.
            cooldown_seconds: Minimum seconds between alerts.
            zcr_threshold: The maximum Zero-Crossing Rate to consider as snoring.
        """
        self.recorder = recorder
        self.threshold = threshold
        self.on_detection = on_detection
        
        # Ensure notifier is always a list
        if notifier is None:
            self.notifier = []
        elif isinstance(notifier, list):
            self.notifier = notifier
        else:
            self.notifier = [notifier]
            
        self.cooldown_seconds = cooldown_seconds
        self.zcr_threshold = zcr_threshold
        self.last_alert_time = 0.0

    def step(self) -> bool:
        """Performs one step of monitoring: read, analyze, and trigger callback.

        Note: This is a synchronous version. It will not call the async notifier.

        Returns:
            True if snoring was detected in this step, False otherwise.
        """
        chunk = self.recorder.read_chunk()
        rms = calculate_rms(chunk)
        
        if rms > self.threshold:
            # Secondary check: ZCR
            zcr = calculate_zcr(chunk)
            logger.info(f"Potential snore detected. RMS: {rms:.2f}, ZCR: {zcr:.4f}")
            
            if zcr <= self.zcr_threshold:
                logger.info(f"[DETECT] Snoring confirmed! RMS: {rms:.2f}, ZCR: {zcr:.4f}")
                if self.on_detection:
                    self.on_detection()
                return True
            else:
                logger.debug(f"Filtered out (high ZCR). RMS: {rms:.2f}, ZCR: {zcr:.4f}")
            
        return False

    async def step_async(self) -> bool:
        """Asynchronous step that also handles Telegram alerts with cooldown.

        Returns:
            True if snoring was detected in this step, False otherwise.
        """
        chunk = self.recorder.read_chunk()
        rms = calculate_rms(chunk)
        
        if rms > self.threshold:
            # Secondary check: ZCR
            zcr = calculate_zcr(chunk)
            logger.info(f"Potential snore detected. RMS: {rms:.2f}, ZCR: {zcr:.4f}")
            
            if zcr <= self.zcr_threshold:
                logger.info(f"[DETECT] Snoring confirmed! RMS: {rms:.2f}, ZCR: {zcr:.4f}")
                if self.on_detection:
                    self.on_detection()
                
                # Handle Notifiers with Cooldown
                if self.notifier:
                    current_time = time.time()
                    if current_time - self.last_alert_time >= self.cooldown_seconds:
                        self.last_alert_time = current_time
                        message = f"Snoring detected! (RMS: {rms:.2f}, ZCR: {zcr:.4f})"
                        for n in self.notifier:
                            try:
                                result = n.send_alert(message)
                                if asyncio.iscoroutine(result):
                                    await result
                            except Exception as e:
                                logger.error(f"Notifier {n.__class__.__name__} failed: {e}")
                        self.last_alert_time = current_time
                    else:
                        logger.debug("Alert skipped due to cooldown.")
                
                return True
            else:
                logger.debug(f"Filtered out (high ZCR). RMS: {rms:.2f}, ZCR: {zcr:.4f}")
            
        return False

    def start_loop(self):
        """Starts a continuous monitoring loop (synchronous)."""
        logger.info(f"Starting monitoring with threshold: {self.threshold}")
        try:
            while True:
                self.step()
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user.")

    async def start_loop_async(self):
        """Starts a continuous monitoring loop (asynchronous)."""
        logger.info(f"Starting async monitoring with threshold: {self.threshold}")
        try:
            while True:
                await self.step_async()
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user.")