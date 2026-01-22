"""Snore detector orchestration module."""

import logging
import time
import asyncio
from typing import Callable, Optional
from snoring.audio_utils import calculate_rms, calculate_zcr, calculate_spectral_centroid

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
        zcr_threshold: float = 0.1,
        spectral_centroid_threshold: float = 1500.0,
        min_consecutive_chunks: int = 3
    ):
        """Initializes the snore detector.

        Args:
            recorder: An object with a read_chunk() method and sample_rate attribute.
            threshold: The RMS threshold above which snoring is detected.
            on_detection: A callback function to execute when snoring is detected.
            notifier: A single notifier instance or a list of notifiers.
            cooldown_seconds: Minimum seconds between alerts.
            zcr_threshold: The maximum Zero-Crossing Rate to consider as snoring.
            spectral_centroid_threshold: Max spectral centroid (Hz) to consider as snoring.
            min_consecutive_chunks: Number of consecutive frames required to confirm snoring.
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
        self.spectral_centroid_threshold = spectral_centroid_threshold
        self.min_consecutive_chunks = min_consecutive_chunks
        
        self.last_alert_time = 0.0
        self.consecutive_snore_chunks = 0

    def _is_snore_chunk(self, chunk: bytes) -> tuple[bool, float, float, float]:
        """Analyzes a chunk to determine if it resembles a snore.
        
        Returns:
            Tuple (is_snore, rms, zcr, centroid)
        """
        rms = calculate_rms(chunk)
        zcr = 0.0
        centroid = 0.0

        if rms > self.threshold:
            zcr = calculate_zcr(chunk)
            
            # Try to get sample rate from recorder, default to 44100 if missing
            sample_rate = getattr(self.recorder, 'sample_rate', 44100)
            centroid = calculate_spectral_centroid(chunk, sample_rate)
            
            logger.debug(f"Analysis: RMS={rms:.2f}, ZCR={zcr:.4f}, Centroid={centroid:.2f}")

            if zcr <= self.zcr_threshold and centroid <= self.spectral_centroid_threshold:
                return True, rms, zcr, centroid
        
        return False, rms, zcr, centroid

    def step(self) -> bool:
        """Performs one step of monitoring: read, analyze, and trigger callback.

        Note: This is a synchronous version. It will not call the async notifier.

        Returns:
            True if snoring was detected in this step, False otherwise.
        """
        chunk = self.recorder.read_chunk()
        is_snore, rms, zcr, centroid = self._is_snore_chunk(chunk)
        
        if is_snore:
            self.consecutive_snore_chunks += 1
            logger.info(f"Potential snore chunk ({self.consecutive_snore_chunks}/{self.min_consecutive_chunks}). RMS: {rms:.2f}, ZCR: {zcr:.4f}, Centroid: {centroid:.2f}")
            
            if self.consecutive_snore_chunks >= self.min_consecutive_chunks:
                # Reset counter after successful detection to avoid spamming every chunk?
                # Or keep it high? Typically, we might want to alert once per "event".
                # For now, let's trigger every chunk once threshold is passed, 
                # but cooldown handles the alerts.
                # To match "consecutive" strictly, we just return True.
                
                # However, for callback `on_detection`, we might want to call it every time
                # we are in a "snoring state".
                logger.info(f"[DETECT] Snoring confirmed! RMS: {rms:.2f}, ZCR: {zcr:.4f}, Centroid: {centroid:.2f}")
                if self.on_detection:
                    self.on_detection()
                return True
        else:
            if self.consecutive_snore_chunks > 0:
                logger.debug(f"Snore sequence broken. Resetting counter.")
            self.consecutive_snore_chunks = 0
            
        return False

    async def step_async(self) -> bool:
        """Asynchronous step that also handles Telegram alerts with cooldown.

        Returns:
            True if snoring was detected in this step, False otherwise.
        """
        chunk = self.recorder.read_chunk()
        is_snore, rms, zcr, centroid = self._is_snore_chunk(chunk)
        
        if is_snore:
            self.consecutive_snore_chunks += 1
            logger.info(f"Potential snore chunk ({self.consecutive_snore_chunks}/{self.min_consecutive_chunks}). RMS: {rms:.2f}, ZCR: {zcr:.4f}, Centroid: {centroid:.2f}")
            
            if self.consecutive_snore_chunks >= self.min_consecutive_chunks:
                logger.info(f"[DETECT] Snoring confirmed! RMS: {rms:.2f}, ZCR: {zcr:.4f}, Centroid: {centroid:.2f}")
                if self.on_detection:
                    self.on_detection()
                
                # Handle Notifiers with Cooldown
                if self.notifier:
                    current_time = time.time()
                    if current_time - self.last_alert_time >= self.cooldown_seconds:
                        self.last_alert_time = current_time
                        message = f"Snoring detected! (RMS: {rms:.2f}, ZCR: {zcr:.4f}, Centroid: {centroid:.0f}Hz)"
                        for n in self.notifier:
                            try:
                                result = n.send_alert(message)
                                if asyncio.iscoroutine(result):
                                    await result
                            except Exception as e:
                                logger.error(f"Notifier {n.__class__.__name__} failed: {e}")
                    else:
                        logger.debug("Alert skipped due to cooldown.")
                
                return True
        else:
            if self.consecutive_snore_chunks > 0:
                logger.debug(f"Snore sequence broken. Resetting counter.")
            self.consecutive_snore_chunks = 0
            
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