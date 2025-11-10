def power2(num):
    if num == 0:
        return False
    return(num & (num - 1)) == 0
num = int(input("Enter the number:"))
if power2(num):
    print(num, "is a power of 2")
else:
    print(num, "is not a power of 2")