with open("tasks.txt","w") as f:
    f.write("Build jarvis\n")
    f.write("Integrate voice recognition\n")
    f.write("Implement task management\n")
    
with open("tasks.txt","r") as f:
    print(f.read())