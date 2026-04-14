FILENAME ="tasks.txt"
#Jarvis to do list App
def load_tasks():
    try:
        with open(FILENAME,"r") as f:
            tasks = f.read().splitlines()
            return tasks
    except FileNotFoundError:
        return[]
    
def save_tasks(tasks):
    with open(FILENAME,"w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Jarvis: You have no tasks right now.")
    else:
        print("Jarvis: Here are your tasks:")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")
            
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Jarvis: Added task'{task}'.")
    
def remove_task(tasks, identifier):
    if identifier.isdigit():
        index = int(identifier) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Jarvis: Removed task '{removed}'.")
        else:
            print("Jarvis: Invalid task number.")
    else:
        if identifier in tasks:
            tasks.remove(identifier)
            save_tasks(tasks)
            print(f"Jarvis: Removed task'{identifier}'.")
        else:
            print("Jarvis: The task is not in the list")
#----Main Loop----
tasks=load_tasks()
print("Jarvis To-Do Assistant (Type 'exit' to stop)")    

while True:
    command = input("Enter command (add / show / remove / exit): ").lower()

    if command=="add":
        new_task = input("What task should I add? ")   
        add_task(tasks,new_task)
    elif command=="show":
        show_tasks(tasks)
    elif command=="remove":
        rem_task =input("Which Task should I Remove? ")
        remove_task(tasks,rem_task)
    elif command=="exit":
        print("Jarvis: Goodbye! saving your tasks for later.")
        break
    else:
        print("Jarvis: Sorry, I don't understand that command.")