#print a clock

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()

for i in range(12):
    alex.shape("square")
    alex.shapesize(0.5)
    alex.color("blue")
    alex.forward(50)
    alex.stamp()
    alex.backward(50)
    alex.left(30)

for i in range (12):
    alex.shape("turtle")
    alex.shapesize(1)
    alex.forward(75)
    alex.stamp()
    alex.backward(75)
    alex.left(30)

wn.exitonclick()
