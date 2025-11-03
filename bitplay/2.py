def isSet(number,n):
    if number&(1<<(n-1)):
        print("is set")
    else:
        print("not set")
number = int(input("ENter a number:"))
n = int(input("Enter a bit number"))
isSet(number,n)