# Take a number and print its table using while
num=int(input("\nEnter a number to print its table: "))
i=1
while i<=10:
    print(f"{num} X {i} = {num*i}")
    i+=1