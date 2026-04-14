tasks = ["Learn Python","Build Jarvis","Test voice input"]

print ("All tasks:", tasks)
print("First task:", tasks[1])
print("Second task:", tasks[0])
print("Last task:", tasks[-1])
tasks.append("Deploy jarvis")
tasks.remove("Build Jarvis")
print ("All tasks:", tasks)
print("First task:", tasks[1])
print("Second task:", tasks[0])
print("Last task:", tasks[-1])