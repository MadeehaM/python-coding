def checkIfSame(num1,num2):
    if((num1^num2) != 0):
        print("Numbers are not the same")
    else:
        print("Numbers are the same")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

checkIfSame(num1,num2)
