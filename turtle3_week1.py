import turtle
wn = turtle.Screen() #set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()#create the tess turtle
tess.pensize(5)
tess.color("blue")

alex = turtle.Turtle() #create the LAex turtle
alex.pensize(5)
alex.color("red")


tess.forward(80) # let tess draw an triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)#complete the triangle and return the cursor to the original direction


tess.right(180) # turn tess arround
tess.forward(80) # move her way from the origim point

alex.forward(50) #make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()









