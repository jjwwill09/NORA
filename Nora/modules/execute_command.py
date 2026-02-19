from modules.log import Log
from modules.training_commands import Train
from modules.tts import text_to_speech
from modules import utils

# Checks for different commands inside the users query
def command_check(text, stop_event=None):
    # Log commands
    if "log.new" in text:
        try:
            Log.new(utils.last_query, utils.nora_response)
        except Exception as e:
            print(f"Error: {e}")
            text_to_speech("There is nothing to log sir")
        if stop_event:
            stop_event.set()
        return True
    elif "log.undo" in text:
        try:
            Log.undo()
        except Exception as e:
            print(f"Error: {e}")
            text_to_speech("Error undoing log")
        if stop_event:
            stop_event.set()
        return True
    elif "log.clear" in text:
        try:
            Log.clear()
        except Exception as e:
            print(f"Error: {e}")
            text_to_speech("Error clearing logs")
        if stop_event:
            stop_event.set()
        return True
    #Train commands
    elif "train.new" in text:
        try:
            Train.new(utils.last_query, utils.nora_response)
        except Exception as e:
            print(f"Error {e}")
            text_to_speech("Error adding data to training data")
        if stop_event:
            stop_event.set()
        return True
    else:
        return False