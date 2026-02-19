import sounddevice as sd
import numpy as np

# Records a short clip from a device_index and returns RMS level, returns nothign if it fails
def measure_device_rms(device_index, duration=0.5, channels=1):
    try:
        dev_info = sd.query_devices(device_index, 'input')
        samplerate = int(dev_info.get('default_samplerate', 44100))
        frames = int(duration * samplerate)
        # Record (this will block until sd.wait())
        recording = sd.rec(frames, samplerate=samplerate, channels=channels, dtype='float32', device=device_index)
        sd.wait()
        # If stereo, reduce to mono by averaging channels
        if recording.ndim > 1:
            recording = np.clip(recording, -1.0, 1.0)
        rms = np.sqrt(np.mean(np.square(recording)))
        return float(rms)
    except Exception as e:
        # Device might be unavailable/busy or unsupported settings
        #print("Device", device_index, "error:", e)
        return None

# Scan all input devices and return info about the microphone with the highest RMS, if no device produces RMS >= the threshold, it returns the device with the highest anyway
def find_most_active_microphone(duration=0.5, min_channels=1, rms_threshold=1e-4):
    devices = sd.query_devices()
    candidates = []
    for idx, dev in enumerate(devices):
        if dev.get('max_input_channels', 0) >= min_channels:
            candidates.append((idx, dev))
        else:
            continue

    if not candidates:
        raise RuntimeError("No input devices found.")

    best = None
    best_rms = -1.0
    results = []
    for idx, dev in candidates:
        rms = measure_device_rms(idx, duration=duration, channels=min_channels)
        results.append((idx, dev, rms))
        if rms is not None and rms > best_rms:
            best_rms = rms
            best = (idx, dev, rms)

    # If no device recorded successfully, raise
    if best is None:
        raise RuntimeError("Failed to record from any input device. Check permissions or device availability.")

    # If best RMS is below threshold, it's likely silence — still return best, but indicate low activity
    return best[0]
