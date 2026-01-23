import pytest
import unittest.mock as mock
from snoring.line_notifier import LineNotifier

def test_line_notifier_init():
    with mock.patch('snoring.line_notifier.MessagingApi') as mock_api:
        notifier = LineNotifier(
            access_token='test_token',
            channel_secret='test_secret',
            user_id='test_user'
        )
        assert notifier.user_id == 'test_user'
        mock_api.assert_called_once()

def test_line_notifier_send_alert_success():
    with mock.patch('snoring.line_notifier.MessagingApi') as mock_api:
        mock_instance = mock_api.return_value
        notifier = LineNotifier(
            access_token='t',
            channel_secret='s',
            user_id='u'
        )
        
        notifier.send_alert("Snore detected")
        
        mock_instance.push_message.assert_called_once()
        args, kwargs = mock_instance.push_message.call_args
        push_message_request = args[0]
        assert push_message_request.to == 'u'
        assert push_message_request.messages[0].text == "Snore detected"

def test_line_notifier_send_alert_failure():
    with mock.patch('snoring.line_notifier.MessagingApi') as mock_api:
        mock_instance = mock_api.return_value
        mock_instance.push_message.side_effect = Exception("API Error")
        
        notifier = LineNotifier(
            access_token='t',
            channel_secret='s',
            user_id='u'
        )
        
        with mock.patch('snoring.line_notifier.logger.error') as mock_log_error:
            notifier.send_alert("Snore detected")
            mock_log_error.assert_called()
            assert "Failed to send LINE alert" in mock_log_error.call_args[0][0]
