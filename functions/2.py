def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulus(x,y):
    return x % y

def flow(x,y):
    return x // y

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Sum:", add(num1,num2))
print("Differnce:", subtract(num1,num2))
print("Product:", multiply(num1,num2))
print("Quotient:", divide(num1,num2))
print("Modulus:", modulus(num1,num2))
print("Flow:", flow(num1,num2))