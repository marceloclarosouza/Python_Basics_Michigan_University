#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

    #An equilateral triangle
    #A square
    #A hexagon (six sides)
    #An octagon (eight sides)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.pensize(3)

for i in range(3):
    alex.shape("turtle")
    alex.color("blue")
    alex.fillcolor("red")
    alex.forward(50)
    alex.left(120)

for i in range(4):
    alex.color("red")
    alex.forward(50)
    alex.right(90)

for i in range(6):
    alex.color("black")
    alex.backward(50)
    alex.right(60)

for i in range(8):
    alex.color("green")
    alex.forward(50)
    alex.right(45)

alex.forward(50)

for i in range(6):
    alex.color("black")
    alex.forward(50)
    alex.left(60)

for i in range(3):
    alex.color("blue")
    alex.left(120)
    alex.forward(50)

wn.exitonclick()