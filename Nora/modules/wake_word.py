import pvporcupine
import pyaudio
import struct

def listen_for_wake_word(mic_index=None):
    # Initialize Porcupine wake word engine
    porcupine = pvporcupine.create(
        access_key="", # Picovoice Key
        keyword_paths=["Hey-Nora_en_windows_v3_0_0\Hey-Nora_en_windows_v3_0_0.ppn"]
    )

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=mic_index,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            # Debug: check input signal
            avg_amplitude = sum(abs(s) for s in pcm) / len(pcm)
            print(f"Mic activity: {avg_amplitude:.1f}", end="\r")

            result = porcupine.process(pcm)
            if result >= 0:
                print("Wake word detected!")
                break           

    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()

