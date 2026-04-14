#  Take user name and time (morning/evening) and greet accordingly
name=input("Enter your name : ")
time=input("Enter time of day (morning/evening) : ")
if time.lower()=="morning":
    print(f"Good Morning, {name}!")
elif time.lower()=="evening":
    print(f"Good Evening, {name}!")
else:
    print(f"Hello {name}! ")