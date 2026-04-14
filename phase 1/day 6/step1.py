with open("notes.txt","w") as f:
    f.write("Hello, this is Jarvis's first memory.\n")
with open("notes.txt","r") as f:
    content = f.read()
    print(content)
with open("notes.txt","a") as f:
    f.write("This is a new line!\n")
with open("notes.txt","r") as f:
    for line in f:
        print("Line:",line.strip())
        