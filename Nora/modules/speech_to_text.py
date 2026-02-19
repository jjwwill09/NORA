import io
import numpy as np
import sounddevice as sd
import soundfile as sf
import librosa
from faster_whisper import WhisperModel

class WhisperTranscriber:
    def __init__(self, model_size="small", device="cuda", compute_type=None, language=None):
        if compute_type is None:
            compute_type = "float16" if device.startswith("cuda") else "int8"

        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        self.language = language
        
    # Turn audio into NumPy array
    def _record_audio(self, mic_device_index=None, duration=5, target_samplerate=16000):
        import warnings
        # Try to get device default sample rate
        try:
            dev_info = sd.query_devices(mic_device_index, 'input')
            safe_samplerate = int(dev_info['default_samplerate'])
        except Exception:
            safe_samplerate = 48000  # fallback if query fails

        print(f"[Listening {duration}s from mic #{mic_device_index} at {safe_samplerate}Hz...]")

        try:
            audio = sd.rec(
                int(duration * safe_samplerate),
                samplerate=safe_samplerate,
                channels=1,
                dtype='float32',
                device=mic_device_index
            )
            sd.wait()
        except sd.PortAudioError:
            # fallback to 48000 if default fails
            print(f"Default sample rate {safe_samplerate}Hz not supported, trying 48000Hz...")
            safe_samplerate = 48000
            audio = sd.rec(
                int(duration * safe_samplerate),
                samplerate=safe_samplerate,
                channels=1,
                dtype='float32',
                device=mic_device_index
            )
            sd.wait()

        audio = audio[:, 0]  # flatten
        # Resample to target for Whisper
        import librosa
        audio_resampled = librosa.resample(audio, orig_sr=safe_samplerate, target_sr=target_samplerate)
        return audio_resampled

    def _transcribe_array(self, audio_array, samplerate=16000):
        # Convert to in-memory WAV
        buf = io.BytesIO()
        sf.write(buf, audio_array, samplerate, format="WAV")
        buf.seek(0)

        segments, info = self.model.transcribe(buf, language=self.language, beam_size=5)
        text_out = " ".join(seg.text for seg in segments if hasattr(seg, "text")).strip()
        return text_out

    def transcribe_from_mic(self, mic_device_index=None, duration=5, target_samplerate=16000):
        audio_array = self._record_audio(mic_device_index, duration, target_samplerate)
        return self._transcribe_array(audio_array, target_samplerate)
