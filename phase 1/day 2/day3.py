print("\n---------------------------------STEP 1---------------------------------\n")
mood="happy"
if mood=="sad":
    print("Great! Let's learn Python today!")
else:
    print("Cheer up! Jarvis is here to help you.")
print("\n---------------------------------STEP 2---------------------------------\n")
command="play music"
if command=="open youtube":
    print("Opening Youtube...")
elif command=="play music":
    print("Playing your favorite song.....")
else:
    print("sorry i don,t understand that command.")
print("\n---------------------------------STEP 3(LOOP)---------------------------------\n")   
for i in range(5):
    print("Jarvis steps",i+1)
print("\n---------------------------------STEP 4---------------------------------\n")
count=1
while count<=3:
    print("Jarvis is listening...attempt",count)
    count+=1
print("\n---------------------------------TASK---------------------------------\n")
command=int(input("Enter a number between 1-100: "))
if command%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
print("\n---------------------------------TASK---------------------------------\n") 
command=["Open Youtube","Play Music","Tell Time","Weather conditions","Exit"]
for cmd in command:
    if cmd=="Open Youtube":
        print("Jarvis: Opening Youtube...")
    elif cmd=="Play Music":
        print("Jarvis: Playing you favorite song...")
    elif cmd=="Tell Time":
        print("Jarvis: The current time is 10:30  AM")
    elif cmd=="Weather conditions":
        print("Jarvis: The weather is sunny with a high of 75°F.")
    elif cmd=="Exit":
        print("Jarvis: Goodbye!")
    else:
        print("Jarvis: Sorry, I don't understand that command.")
print("\n---------------------------------TASK---------------------------------\n")
command=input("Enter a command: ")
if command=="Time":
    print("Jarvis: The current time is 10:30 AM")
elif"Youtube":
    print("Jarvis: Opening Youtube...")
elif "exit":
    print("Jarvis: Goodbye!")
else:
    print("Jarvis: Sorry, I don't understand that command.")