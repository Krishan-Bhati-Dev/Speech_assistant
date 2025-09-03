# ==================== IMPORTING REQUIREMENTS ====================
import speech_recognition as sr     # For speech-to-text (recognizing voice)
import pyttsx3                      # For text-to-speech (assistant speaking)
import datetime                     # For time/date functionality
import webbrowser                   # To open websites
import sys                          # To exit the program
import os                           # To open system apps/folders
import pyautogui                    # For GUI automation (currently unused)
from playsound import playsound     # To play audio files (currently unused)
import pywhatkit                    # To search/play YouTube, send WhatsApp msg, etc.
import wikipedia                    # To fetch summaries from Wikipedia


# ==================== TEXT-TO-SPEECH (TTS) ====================
def speak(text: str):
    """
    Converts text into speech and prints it on console.
    NOTE: Here engine is re-initialized every time (not optimal).
    """
    print("Assistant:", text)

    # Initialize speech engine each time (slower, but works reliably in some cases)
    engine = pyttsx3.init('sapi5')   # 'sapi5' = Windows speech API
    engine.setProperty("rate", 170)  # Speed of the voice
    engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

    # Get available voices and set the first one
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

    # Stop the engine (not necessary, but avoids resource locking)
    engine.stop()


# ==================== SPEECH RECOGNITION ====================
recognizer = sr.Recognizer()   # Create recognizer instance

def listen():
    """
    Listens through the microphone, processes audio, and converts it to text.
    Handles errors like timeout, unknown speech, or network issues.
    """
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise

        try:
            # Listen for voice (max 5 sec of silence and 5 sec total phrase)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            # Use Google's speech recognition
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower().strip()

        except sr.WaitTimeoutError:
            speak("No speech detected.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""


# ==================== COMMAND ROUTER ====================
def process_command(command: str):
    """
    Takes a recognized voice command and performs the appropriate action.
    """

    if not command:
        return   # Skip if empty command

    # ---- TIME ----
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # ---- DATE ----
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    # ---- SEARCH ----
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")

    # ---- RECYCLE BIN ----
    elif "recycle bin" in command:
        speak("Opening recycle bin in safe mode.")
        os.system("start shell:RecycleBinFolder")  # Opens Recycle Bin
        print("SAFE TEST MODE: Recycle Bin opened, but no files were deleted.")
        speak("Recycle bin opened. No files were deleted, this is just a test.")

    # ---- YOUTUBE ----
    elif "open youtube" in command or "play" in command:
        speak("What do you want me to play?")
        query = listen()
        if query:
            speak(f"Playing {query} on YouTube.")
            pywhatkit.playonyt(query)   # Opens YouTube and plays top result

    # ---- WIKIPEDIA ----
    elif "wikipedia" in command:
        speak("What is your query?")
        query = listen()
        if query:
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except wikipedia.DisambiguationError:
                speak("Your query is too broad. Please be more specific.")
            except wikipedia.PageError:
                speak("I couldn't find any information on that topic.")

    # ---- CHATGPT ----
    elif "chat gpt" in command:
        speak("Opening ChatGPT in browser.")
        url = "https://chat.openai.com/"
        webbrowser.open(url)

    # ---- EXIT ----
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        sys.exit(0)

    # ---- UNKNOWN COMMAND ----
    else:
        speak("I can tell you the time, date, play music, or search the web. Please try again.")


# ==================== MAIN LOOP ====================
if __name__ == "__main__":
    speak("How can I help you?")
    while True:
        command = listen()          # Listen for user input
        process_command(command)    # Process the input and respond
