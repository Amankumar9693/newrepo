a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
o=input("Enter operator(+,-,*,/,//,%,**) : ")
if o =='+':
    print(a+b)
elif o =='-':
    print(a-b)
elif o =='*':
    print(a*b)
elif o =='/':
    print(a/b)
elif o =='%':
    print(a%b)
elif o =='//':
    print(a//b)
elif o =='**':
    print(a**b)
else:
    print("Invalid operator")
# Grade system
marks=int(input("Enter your marks: "))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
elif marks>=40:
    print("E")
else:
    print("F")