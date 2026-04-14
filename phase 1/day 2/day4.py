def greet():
    print("\nHello, i am your assistant Jarvis!")
greet()
print("\n---------------------------------STEP 2---------------------------------\n")
def greet_user(name):
    print(f"Hello {name}, welcome back!\n")
greet_user("Aman")
greet_user("Tony Stark")
print("\n---------------------------------STEP 3---------------------------------\n")
def add_numbers(a,b):
    return a+b
result = add_numbers(5,7)
print("Sum is:", result)
print("\n---------------------------------STEP 4---------------------------------\n")
def jarvis_command(command):
    if command == "time":
        return "The time is 10:30 AM"
    elif command =="youtube":
        return "Opening Youtube..."
    else:
        return "Sorry, I don't understand."
    
print(jarvis_command("time"))
print(jarvis_command("youtube"))
print(jarvis_command("play music"))
print("\n---------------------------------TASK---------------------------------\n")
def assistant_speak():
   msg = input()
   print("Jarvis says: ", msg)
assistant_speak()
print("\n---------------------------------TASK---------------------------------\n")
def multiply(a,b):
    return a*b
a=int(input("first number: "))
b=int(input("second number: "))
result=multiply(a,b)
print("Product is:",result)
