import turtle
wn = turtle.Screen()
elan = turtle.Turtle()
distance = 50
angle = 90
for _ in range(15):
    elan.forward(distance)
    elan.right(angle)
    distance += 10
    angle -= 3