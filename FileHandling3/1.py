with open('new.txt', 'w') as file:
    file.write("Hi I am 5 years old")
file.close()

with open('new.txt', 'r') as file:
    data=file.readlines()
    print("Words are:")
    for line in data:
        word = line.split()
        print(word)
file.close