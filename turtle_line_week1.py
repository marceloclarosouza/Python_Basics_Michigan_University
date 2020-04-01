#create the turtle, set the shape to "turtle", and pick up the pen. Then the turtle should repeat the following three times: go forward 50 pixels and leave a copy of the turtle at the current position. After the loop, set the window to close when the user clicks in it.

import turtle
wn = turtle.Turtle()
nikea = turtle.Turtle()
nikea.shape("turtle")
nikea.penup()

for i in range (5):
    nikea.forward(50)
    nikea.stamp()
wn.exitonlyclick()