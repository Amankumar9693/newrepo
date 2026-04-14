name=input("Enter your name: ")
with open("user.txt","w") as f:
    f.write(name+"\n")
print("Your name has been saved to user.txt!")