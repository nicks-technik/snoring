"""Fritz!Box notifier module for internal calls."""

import logging
import asyncio
from fritzconnection import FritzConnection

logger = logging.getLogger(__name__)

class FritzNotifier:
    """Triggers an internal call via Fritz!Box TR-064."""

    def __init__(
        self,
        address: str,
        user: str,
        password: str,
        target_number: str,
        ring_duration: int = 10
    ):
        """Initializes the Fritz!Box connection.

        Args:
            address: IP address of the Fritz!Box.
            user: Username for authentication.
            password: Password for authentication.
            target_number: Internal number to dial (e.g., '**610').
            ring_duration: How long the phone should ring in seconds.
        """
        self.target_number = target_number
        self.ring_duration = ring_duration
        self.fc = FritzConnection(
            address=address,
            user=user,
            password=password,
            use_tls=True,
            timeout=10
        )

    async def send_alert(self, message: str):
        """Triggers an internal call and hangs up after ring_duration.

        Args:
            message: Ignored, but kept for interface compatibility.
        """
        try:
            logger.info(f"Triggering Fritz!Box call to {self.target_number}...")
            # Start dialing
            self.fc.call_action(
                'X_VoIP1',
                'X_AVM-DE_DialNumber',
                **{'NewX_AVM-DE_PhoneNumber': self.target_number}
            )
            
            # Wait for ring duration
            await asyncio.sleep(self.ring_duration)
            
            # Hang up
            self.fc.call_action('X_VoIP1', 'X_AVM-DE_DialHangup')
            logger.info("Fritz!Box call ended.")
            
        except Exception as e:
            logger.error(f"Failed to trigger Fritz!Box call: {e}")
