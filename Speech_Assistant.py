# ==================== IMPORTS ====================
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys
import os
import pywhatkit
import wikipedia


# ==================== TEXT-TO-SPEECH ENGINE ====================
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)


def speak(text: str):
    """Convert text to speech + print it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ==================== SPEECH RECOGNITION ====================
recognizer = sr.Recognizer()

def listen():
    """Listen through microphone and return recognized speech."""
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.4)

        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            speak("Internet error. Please check your connection.")
            return ""


# ==================== COMMAND HANDLER ====================
def process_command(command: str):

    if not command:
        return

    # ---- TIME ----
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # ---- DATE ----
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    # ---- GOOGLE SEARCH ----
    elif "search" in command:
        speak("What do you want to search?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the results for {query}")

    # ---- OPEN RECYCLE BIN ----
    elif "recycle bin" in command:
        speak("Opening recycle bin.")
        os.system("start shell:RecycleBinFolder")

    # ---- PLAY YOUTUBE VIDEO ----
    elif command.startswith("play"):
        query = command.replace("play", "").strip()
        if query:
            speak(f"Playing {query}")
            pywhatkit.playonyt(query)
        else:
            speak("What should I play?")
            query = listen()
            if query:
                pywhatkit.playonyt(query)

    # ---- OPEN YOUTUBE ----
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    # ---- WIKIPEDIA ----
    elif "wikipedia" in command:
        speak("What topic?")
        query = listen()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2)
                speak(summary)
            except:
                speak("Could not find information on that topic.")

    # ---- OPEN CHATGPT ----
    elif "chat gpt" in command or "chatgpt" in command:
        speak("Opening ChatGPT.")
        webbrowser.open("https://chat.openai.com")

    # ---- EXIT ----
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        sys.exit()

    # ---- UNKNOWN ----
    else:
        speak("I can tell the time, search, open YouTube, or play music. Try again.")


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":
    speak("How can I help you?")
    while True:
        command = listen()
        process_command(command)
