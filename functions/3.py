def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))

if num < 0:
    print("Number must be above zero")
elif num == 0:
    print("Factorial of zero is 1")
else:
    print("The factorial of", num, "is", factorial(num))
    