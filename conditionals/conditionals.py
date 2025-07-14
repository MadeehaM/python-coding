number = int(input("Please enter a number:"))
print("Number to be checked:" , number)

if number%2==0:
    if number>50:
        print("This is a bigger number")
    else:
        print("This is a smaller number")
    print("This is an even number")
else:
    print("This is an odd number")