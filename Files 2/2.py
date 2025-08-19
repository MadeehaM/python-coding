file = open('white.txt', 'r')
print("First Line:")
print(file.readline())
file.close()

file = open('white.txt', 'r')
print("First 3 lines:")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('white.txt', 'r')
print("Looping through lines:")
for line in file:
    print(line)
file.close()