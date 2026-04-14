import speech_recognition as sr
import pyttsx3
# import pyaudio

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
   engine.say(text)
   engine.runAndWait() 
   
with sr.Microphone() as source:
    speak("Hello, I am Jarvis. Say Something.")
    print("Jarvis: Listening...")
    audio = recognizer.listen(source)
    
try:
    command = recognizer.recognize_google(audio)
    print("You said: ", command)
    speak(f"You said {command}")
except sr.UnknownValueError:
    speak("Sorry, I didn't catch that.")