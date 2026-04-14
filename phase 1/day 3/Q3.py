# Keep asking user for a number until they enter 0
c=0
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    c+=1
print(c)
# Count how many numbers user entered