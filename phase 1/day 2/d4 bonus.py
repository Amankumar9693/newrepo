from datetime import datetime
def jarvis(command):
    if command =="time":
        now=datetime.now().strftime("%H:%M:%S")
        return f"The time is [ {now} ]"
    elif command == "youtube":
        return "Opening YouTube..."
    
    elif command == "exit":
        return "Goodbye! Jarvis shutting down."
    
    else:
        return "Sorry, I don't understand that command."
for cmd in ["time", "youtube", "play music", "exit"]:
    print(jarvis(cmd))
