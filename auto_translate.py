# Every comment written was written by me to show that I know whats going on.

# Before runnig, ensure that googletrans   and   Translator    bave been pip installed 

import keyboard   # Captures in real time instead of waiting for user to press enter.
import time       # Will be used to both check when the user last typed, and to pause a little bit so the PC doesn't lag a bunch.
import sys
import re
from googletrans import Translator       # Literally just a tool taken straight out the google library to make it actually translate.
from threading import Thread             #Thread used to run multiple loops at one time. This allows it to translate in the background while you're still activley typing.

translator = Translator()   # Make an actual translate object to call upon.
typed_text = ""              # Makes it so that every key press will be added to build the full sentence.
last_type_time = 0          # Stores a timestamp of the last time a key was presseed and makes it so that the program will wait till the user stops typing before calling it.
debounce_delay = 0.5       # Makes a half second delay for the translation after the previous key press. Withou it, everythings gonna be slow and unnecessary.
last_translation = ""
display_text = ""



def clean_text_for_translation(text):
    # Add a space after punctuation if it's missing
    text = re.sub(r'([.!?])([^\s])', r'\1 \2', text)
    return text

def translate_loop():
    global typed_text, last_type_time, last_translation
    while True:
        if time.time() - last_type_time > debounce_delay and typed_text.strip():
            try:
                translation = translator.translate(clean_text_for_translation(typed_text), src="auto", dest="en").text
                if translation != last_translation:
                    last_translation = translation
            except Exception as e:
                last_translation = f"Translation failed: {e}"
        time.sleep(0.1)

def display_loop():
    global typed_text, last_translation, display_text
    while True:
        new_display = f"You: {typed_text} | English: {last_translation}"
        if new_display != display_text:
            sys.stdout.write("\r" + " " * 120 + "\r")  # clear line
            sys.stdout.write(new_display)
            sys.stdout.flush()
            display_text = new_display
        time.sleep(0.05)

def on_key(event):
    global typed_text, last_type_time
    punctuation_space = {".", ",", "!", "?", ";", ":"}  # add more if needed

    if event.name == "esc":
        print("\nExiting translator...")
        keyboard.unhook_all()
        sys.exit()
    elif event.name == "backspace":
        typed_text = typed_text[:-1]
    elif event.name == "space":
        typed_text += " "
    elif event.name in punctuation_space:
        typed_text += event.name + " "  # add a space after punctuation
    elif len(event.name) == 1:
        typed_text += event.name
    last_type_time = time.time()


print("\nLive Translator (Press ESC to quit)\n")
print("Just type anything to get started\n")

# Start translation thread
Thread(target=translate_loop, daemon=True).start()
# Start display thread
Thread(target=display_loop, daemon=True).start()

# Hook keyboard events
keyboard.on_press(on_key)

# Keep the program alive
keyboard.wait("esc")
