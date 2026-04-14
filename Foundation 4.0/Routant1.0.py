import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import wikipedia
import pyautogui
import time
from openai import OpenAI

# API KEY (set your key here or use environment variable)
client = OpenAI(api_key="YOUR_API_KEY")

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

def ask_ai(command):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": command}]
    )
    return response.choices[0].message.content

speak("Jarvis activated")

while True:

    command = listen()

    # skip empty input
    if command == "":
        continue

    # =========================
    # 🔥 MULTI-COMMAND HANDLING
    # =========================
    if "and" in command:
        parts = command.split("and")

        for part in parts:
            part = part.strip()

            # OPEN
            if "open" in part:
                if "chrome" in part:
                    speak("Opening Chrome")
                    os.system("start chrome")

                elif "youtube" in part:
                    speak("Opening YouTube")
                    webbrowser.open("https://youtube.com")

            # SEARCH
            elif "search youtube" in part:
                query = part.replace("search youtube", "").strip()
                speak("Searching YouTube " + query)
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

            elif "search" in part:
                query = part.replace("search for", "").replace("search", "").strip()
                speak("Searching " + query)
                webbrowser.open(f"https://www.google.com/search?q={query}")

            # CREATE FOLDER
            elif "create folder" in part:
                name = part.replace("create folder", "").strip()
                try:
                    os.mkdir(name)
                    speak("Folder created")
                except FileExistsError:
                    speak("Folder already exists")

        continue  # important to skip further processing

    # =========================
    # 🔹 SINGLE COMMANDS
    # =========================

    # OPEN
    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # SEARCH
    elif "search youtube" in command:
        query = command.replace("search youtube", "").strip()
        speak("Searching YouTube " + query)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif "search" in command:
        query = command.replace("search for", "").replace("search", "").strip()
        speak("Searching " + query)
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # CREATE FOLDER
    elif "create folder" in command:
        name = command.replace("create folder", "").strip()
        try:
            os.mkdir(name)
            speak("Folder created")
        except FileExistsError:
            speak("Folder already exists")

    # KNOWLEDGE
    elif "what is" in command:
        query = command.replace("what is", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find information")

    # EXIT
    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        break

    # =========================
    # 🧠 AI FALLBACK
    # =========================
    elif len(command) > 2:
        answer = ask_ai(command)
        speak(answer)