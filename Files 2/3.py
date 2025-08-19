First = open('white.txt', 'r')
Second = open('black.txt', 'w')

for line in First.readlines():
    if not (line.startswith('File')):
        print(line)
        Second.write(line)

First.close()
Second.close()