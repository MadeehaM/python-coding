firstfile = input("Enter the first file:")
secondfile = input("Enter the second file:")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print("First file before appending:\n", f1.read())
print("Second file before appending:\n", f2.read())

f1.close()
f2.close()

f1= open(firstfile, 'a+')
f2= open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("First file after appending:\n", f1.read())
print("Second file after appending:\n", f2.read())

f1.close()
f2.close()


















