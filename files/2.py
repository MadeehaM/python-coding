file = open('white.txt', 'r')

Counter = 0

Content = file.read()

CoList = Content.split("\n")

for i in CoList:
    if i.strip():
        Counter += 1

file.close()
print("This is the number of lines:")
print(Counter)