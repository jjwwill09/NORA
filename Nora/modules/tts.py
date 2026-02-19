import pyttsx3 as ps

# Text-to-speech method
def text_to_speech(input):
    #The input is the text
    text = input

    print("Speaking:", text)

    # Initializes pyttsx3 then gets a built in voice property and uses the say method with that voice until its finished speaking
    tts = ps.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[1].id)
    tts.say(text)
    tts.runAndWait()