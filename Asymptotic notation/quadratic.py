def ONSquareTime(n): #quadratin-square of input
    iteration = 0
    for i in range(n):
        for j in range(n):
            iteration += 1
            print(f"Iteration {iteration}: (i = {i}, j={j}) ")
    print("Total iterations done:",iteration)

ONSquareTime(3)
ONSquareTime(4)
ONSquareTime(5)