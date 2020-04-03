#A turtle’s pen can be picked up or put down. This allows us to move a turtle to a different place without drawing a line. The methods are up and down. Note that the methods penup and pendown do the same thing.
#Every turtle can have its own shape. The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
#You can speed up or slow down the turtle’s animation speed. (Animation controls how quickly the turtle turns and moves forward). Speed settings can be set between 1 (slowest) to 10 (fastest).
#A turtle can “stamp” its footprint onto the canvas, and this will remain after the turtle has moved somewhere else. Stamping works even when the pen is up.

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")

dist = 5
alex.up()# same penup
for i in range(50):
    alex.stamp() #leav an impression on the canvas
    alex.forward(dist)
    alex.right(24)
    alex.speed(5)
    dist += 2
wn.exitonclick()

