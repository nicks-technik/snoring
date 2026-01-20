import pytest
import unittest.mock as mock
from snoring.x_notifier import XNotifier

def test_x_notifier_init():
    with mock.patch('tweepy.Client') as mock_client:
        notifier = XNotifier(
            api_key='ak',
            api_secret='as',
            access_token='at',
            access_token_secret='axs',
            recipient_id='rid'
        )
        assert notifier.recipient_id == 'rid'
        mock_client.assert_called_once_with(
            consumer_key='ak',
            consumer_secret='as',
            access_token='at',
            access_token_secret='axs'
        )

def test_x_notifier_send_alert_success():
    with mock.patch('tweepy.Client') as mock_client:
        mock_instance = mock_client.return_value
        notifier = XNotifier(
            api_key='ak',
            api_secret='as',
            access_token='at',
            access_token_secret='axs',
            recipient_id='rid'
        )
        
        notifier.send_alert("Snore detected")
        
        mock_instance.create_direct_message.assert_called_once_with(
            participant_id='rid',
            text="Snore detected"
        )

def test_x_notifier_send_alert_failure():
    with mock.patch('tweepy.Client') as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.create_direct_message.side_effect = Exception("API Error")
        
        notifier = XNotifier(
            api_key='ak',
            api_secret='as',
            access_token='at',
            access_token_secret='axs',
            recipient_id='rid'
        )
        
        with mock.patch('snoring.x_notifier.logger.error') as mock_log_error:
            notifier.send_alert("Snore detected")
            mock_log_error.assert_called()
            assert "Failed to send X.com alert" in mock_log_error.call_args[0][0]
