import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("red")

def move_forward():
    t.forward(100)

screen.listen()
screen.onkey(move_forward, "space")

turtle.mainloop()