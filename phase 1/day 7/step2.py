import speech_recognition as sr
import pyaudio
print("PyAudio is installed correctly!")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Jarvis: Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
except sr.UnknownValueError:
    print("Jarvis: Sorry, I didn't catch that.")