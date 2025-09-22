def Online(n): #Linear time complexity-the number of steps depends on the input
    for i in range(1, n+1):
        print("Iteration:",i)
    print("Total iterations done:",n)


Online(5)
Online(10)
Online(20)