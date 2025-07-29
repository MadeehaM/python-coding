first = (1, "hello", 3, 9)
print(first)

first = ("dog", [4,2,8], (7,9,3))
print(first)

first=("a", "b", "c", "d", "e")
print(first[1])
print(first[3])

new = ("red", [0,3,4], (2,8,1))

print("Nested tuple")
print(new[2][2])
print(new[1][0])

print("Sliced:", new[1:2])

for letter in (first):
    print("hello", letter)