import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time
from datetime import datetime
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_by_time():
    hour = datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif c.startswith("play"):
        parts = c.split(" ")
        if len(parts) > 1:
            song = parts[1]
            if song in musicLibrary.music:
                webbrowser.open(musicLibrary.music[song])
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please specify a song name.")
    elif "news" in c:
        speak("Opening top news headlines for you.")
        webbrowser.open("https://timesofindia.indiatimes.com/india/timestopten.cms")
    elif "exit" in c or "stop" in c:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    greet_by_time()
    speak("Jarvis is online and listening...")
    while True:
        print("Listening...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
            command = recognizer.recognize_google(audio)
            print("Heard:", command)

            if "jarvis" in command.lower():
                speak("Yes, I'm here.")
                clean_command = command.lower().replace("jarvis", "").strip()
                processCommand(clean_command)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Speech recognition service error:", e)
        except Exception as e:
            print("Error:", e)
            speak("There was an error. Please check your setup.")
            time.sleep(2)