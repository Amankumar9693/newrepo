# Ask user what they want to open (Chrome / Notepad / Calculator) and print:
command=input("Enter the application you want to open (Chrome/Notepad/Calculator): ")
if command.lower()=='chrome':
    print("Opening chrome...")
elif command.lower()=='notepad':
    print("Opening Notepad...")
elif command.lower()=='calculator':
    print("Opening Calculator...")
else:
    print("Invalid application")

