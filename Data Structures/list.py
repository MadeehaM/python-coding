colors = ["Pink", "Red", "Orange", "Blue", "Green"]

print("List length:", len(colors))

print("First Element", colors[0])

print("Last Element", colors[-1])

colors.append("white")
print("Updated list:", colors)

colors.remove("Orange")
print("After removing orange:", colors)

colors.sort()
print("Sorted list:", colors)

colors.pop(-1)
print("List after removing index -1:", colors)

colors.reverse()
print("Reversed list:", colors)

print("Multiplication of list:", colors*2)

print("Sliced list from green", colors[2:-1])

colors.clear()
print("List after clearing:", colors)