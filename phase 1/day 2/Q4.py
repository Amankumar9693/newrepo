# Take a command string and print what JARVIS should do:
# “open chrome”
# “play music”
# “shutdown”
command = input("Enter a command for JARVIS: ")
if command=="open chrome":
    print("Command: opening Chrome.")
elif command=="play music":
    print("Command: playing music.")
elif command=="shutdown":
    print("Command: shutting down.")
else:
    print("Command not recognized.")