"""Snore detector orchestration module."""

import logging
from typing import Callable, Optional
from snoring.audio_utils import calculate_rms

logger = logging.getLogger(__name__)

class SnoreDetector:
    """Orchestrates audio recording and analysis to detect snoring."""

    def __init__(
        self,
        recorder,
        threshold: float,
        on_detection: Optional[Callable[[], None]] = None
    ):
        """Initializes the snore detector.

        Args:
            recorder: An object with a read_chunk() method.
            threshold: The RMS threshold above which snoring is detected.
            on_detection: A callback function to execute when snoring is detected.
        """
        self.recorder = recorder
        self.threshold = threshold
        self.on_detection = on_detection

    def step(self) -> bool:
        """Performs one step of monitoring: read, analyze, and trigger callback.

        Returns:
            True if snoring was detected in this step, False otherwise.
        """
        chunk = self.recorder.read_chunk()
        rms = calculate_rms(chunk)
        
        if rms > self.threshold:
            logger.info(f"[DETECT] Snoring detected! RMS: {rms:.2f}")
            if self.on_detection:
                self.on_detection()
            return True
            
        return False

    def start_loop(self):
        """Starts a continuous monitoring loop.
        
        This method is blocking and should be interrupted by KeyboardInterrupt.
        """
        logger.info(f"Starting monitoring with threshold: {self.threshold}")
        try:
            while True:
                self.step()
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user.")
