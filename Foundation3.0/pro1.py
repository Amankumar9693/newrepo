while True:
    try:
        command = input("Jarvis >>> ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nJarvis stopped.")
        break

    if command == "exit":
        print("Goodbye! Jarvis shutting down.")
        break
    elif command == "open chrome":
        print("Opening Google Chrome...")
    elif command == "open youtube":
        print("Opening YouTube...")
    elif command == "play music":
        print("Playing music...")
    else:
        print("Sorry, I don't understand that command.")
