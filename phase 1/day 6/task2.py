FILENAME="user.txt"
try: 
    with open(FILENAME,"r") as f:
        name= f.read().strip()
    if name:
        print(f"Jarvis: welcome back,{name}!")
    else:
        raise FileNotFoundError
except FileNotFoundError:
    name= input("Jarvis: Hello! what's your name?")
    with open(FILENAME,"w") as f:
        f.write(name)
    print(f"Jarvis: Nice to meet you,{name}.I'll remember your name for next time.")

