file = open('white.txt', 'r')
print(file.read())
file.close()

file = open('white.txt', 'r')
print("\n Read in parts \n")
print(file.read(10))
file.close()

file = open('white.txt', 'a')
file.write("\n Hi I am 1 year old")
file.close()