import unittest.mock as mock
import pytest
import pyaudio
from snoring.audio_recorder import AudioRecorder

@mock.patch('snoring.audio_recorder.pyaudio.PyAudio')
def test_audio_recorder_init(mock_pyaudio):
    mock_instance = mock_pyaudio.return_value
    recorder = AudioRecorder(sample_rate=44100, chunk_size=1024)
    
    mock_pyaudio.assert_called_once()
    mock_instance.open.assert_called_once()
    args, kwargs = mock_instance.open.call_args
    assert kwargs['rate'] == 44100
    assert kwargs['frames_per_buffer'] == 1024

@mock.patch('snoring.audio_recorder.pyaudio.PyAudio')
def test_audio_recorder_read(mock_pyaudio):
    mock_instance = mock_pyaudio.return_value
    mock_stream = mock_instance.open.return_value
    mock_stream.read.return_value = b'\x00\x00' * 1024
    
    recorder = AudioRecorder(chunk_size=1024)
    data = recorder.read_chunk()
    
    assert data == b'\x00\x00' * 1024
    mock_stream.read.assert_called_once_with(1024, exception_on_overflow=False)

@mock.patch('snoring.audio_recorder.pyaudio.PyAudio')
def test_audio_recorder_close(mock_pyaudio):
    mock_instance = mock_pyaudio.return_value
    mock_stream = mock_instance.open.return_value
    
    recorder = AudioRecorder()
    recorder.close()
    
    mock_stream.stop_stream.assert_called_once()
    mock_stream.close.assert_called_once()
    mock_instance.terminate.assert_called_once()
