import pytest
import unittest.mock as mock
from snoring.fritz_notifier import FritzNotifier

@pytest.mark.asyncio
async def test_fritz_notifier_init():
    with mock.patch('snoring.fritz_notifier.FritzConnection') as mock_conn:
        notifier = FritzNotifier(
            address='192.168.178.1',
            user='user',
            password='password',
            target_number='**610',
            ring_duration=2
        )
        mock_conn.assert_called_once_with(
            address='192.168.178.1',
            user='user',
            password='password',
            use_tls=True,
            timeout=10
        )
        assert notifier.target_number == '**610'
        assert notifier.ring_duration == 2

@pytest.mark.asyncio
async def test_fritz_notifier_send_alert_success():
    with mock.patch('snoring.fritz_notifier.FritzConnection') as mock_conn:
        mock_instance = mock_conn.return_value
        notifier = FritzNotifier(
            address='1.1.1.1',
            user='u',
            password='p',
            target_number='**610',
            ring_duration=1
        )
        
        with mock.patch('asyncio.sleep', return_value=None) as mock_sleep:
            await notifier.send_alert("Snore detected")
            
            # Check dial call
            mock_instance.call_action.assert_any_call(
                'X_VoIP1',
                'X_AVM-DE_DialNumber',
                **{'NewX_AVM-DE_PhoneNumber': '**610'}
            )
            
            # Check sleep
            mock_sleep.assert_called_once_with(1)
            
            # Check hangup call
            mock_instance.call_action.assert_any_call(
                'X_VoIP1',
                'X_AVM-DE_DialHangup'
            )

@pytest.mark.asyncio
async def test_fritz_notifier_send_alert_failure():
    with mock.patch('snoring.fritz_notifier.FritzConnection') as mock_conn:
        mock_instance = mock_conn.return_value
        mock_instance.call_action.side_effect = Exception("Dial failed")
        
        notifier = FritzNotifier(
            address='1.1.1.1',
            user='u',
            password='p',
            target_number='**610',
            ring_duration=1
        )
        
        with mock.patch('snoring.fritz_notifier.logger.error') as mock_log_error:
            await notifier.send_alert("Snore detected")
            mock_log_error.assert_called()
            assert "Failed to trigger Fritz!Box call" in mock_log_error.call_args[0][0]
