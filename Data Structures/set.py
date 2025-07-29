first = {1,2,3,4,5,6}
print("Set:", first)

first.add(7)
print("New set:", first)

set1= first
set2= {4,5,6,7}

print("Set 1:", set1)
print("Set 2:", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))
print("Union")
print(set1.union(set2))
print("Intersection")
print(set1.intersection(set2))
