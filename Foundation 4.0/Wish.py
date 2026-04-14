import pyttsx3
import datetime

engine = pyttsx3.init()

def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        text = "Good Morning Aman!"
    elif hour < 18:
        text = "Good Afternoon Aman!"
    else:
        text = "Good Evening Aman!"

    engine.say(text)
    engine.runAndWait()

greet()