import turtle
sc=turtle.Screen()
t=turtle.Turtle()
colors = ['red', 'purple', 'blue', 'pink', 'brown', 'yellow']
sc.bgcolor('black')
t.speed('fastest')
t.hideturtle()
for i in range(2):
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
    t.right(239)
    for x in range(200,0,-1):
        t.pencolor('black')
        t.width(x/100 + 7) 
        t.forward(x)
        t.right(59)