"""Audio recorder module for snoring detection."""

import pyaudio

class AudioRecorder:
    """Wraps PyAudio to record audio chunks from the default input device."""

    def __init__(self, sample_rate: int = 44100, chunk_size: int = 1024):
        """Initializes the audio recorder and opens the stream.

        Args:
            sample_rate: The sample rate for recording (default: 44100).
            chunk_size: The size of each audio chunk (default: 1024).
        """
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )

    def read_chunk(self) -> bytes:
        """Reads a chunk of audio data from the stream.

        Returns:
            The raw audio data as bytes.
        """
        return self.stream.read(self.chunk_size, exception_on_overflow=False)

    def close(self):
        """Stops the stream and terminates the PyAudio instance."""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.audio:
            self.audio.terminate()
