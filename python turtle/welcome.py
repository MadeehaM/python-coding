import turtle

turtle.Screen().bgcolor("red")
sc=turtle.Screen()
sc.setup(1000,500)

turtle.title("Welcome to turtle")
board=turtle.Turtle()

for i in range(8):
    board.forward(50)
    board.left(45)
    i=i+1