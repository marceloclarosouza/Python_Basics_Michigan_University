#create the turtle, set the shape to "turtle", and pick up the pen. Then the turtle should repeat the following ten times: go forward 50 pixels, leave a copy of the turtle at the current position, reverse for 50 pixels, and then turn right 36 degrees. After the loop, set the window to close when the user clicks in it

import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)

for size in range(10):
    jose.forward(100)
    jose.stamp()
    jose.forward(-100)
    jose.right(36)
wn.exitonclick()