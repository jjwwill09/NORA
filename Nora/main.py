import concurrent.futures
import threading

from modules.llm import LLM
from modules.wake_word import listen_for_wake_word
from modules.tts import text_to_speech
from modules.find_mic import find_most_active_microphone
from modules.execute_command import command_check
from modules.speech_to_text import WhisperTranscriber

from modules.training_commands import Train
from modules.log import Log
from modules import utils

# Method runs whenever the wake word is detected
def handle_wake_word():
    text_to_speech("I'm listening.")
    
    # Transcribes your voice into text
    text = transcriber.transcribe_from_mic(mic_device_index=mic_index, duration=5)
    print("You said:", text)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        stop_event = threading.Event()

        # Start both tasks at once
        future_command = executor.submit(command_check, text, stop_event) 
        future_response = executor.submit(LLM, text, stop_event)

        # Wait for the first one to finish
        done, pending = concurrent.futures.wait(
            [future_command, future_response],
            return_when=concurrent.futures.FIRST_COMPLETED
        )

        # Determine which one finished first
        if future_command in done and future_command.result() is True:
            print("Command recognized — cancelling LLM and skipping response.")
            for p in pending:
                p.cancel()
            return  # exit early, don't continue the rest

        # Otherwise, wait for LLM to finish normally
        response = list(future_response.result())
    
    # Says nora's response outloud while also logging the results
    utils.last_query = text
    utils.nora_response = response[1]
    text_to_speech(utils.nora_response)
    elapsed_time = response[0]

    Log.add_data(elapsed_time, text)

# Starts by finding the audio device then starts the main loop
if __name__ == "__main__":
    text_to_speech("Finding your audio device")
    mic_index = find_most_active_microphone(duration=0.5)
    transcriber = WhisperTranscriber(model_size="small", device="cpu")
    text_to_speech(f"Using mic index {mic_index}")

    # Listens for wake word, then continues the process after heard
    while True:
        listen_for_wake_word(mic_index=mic_index)

        handle_wake_word()
