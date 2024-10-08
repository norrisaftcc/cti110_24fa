# CTI 110
# P1BONUS - Turtles
# Name
# 9/26/24

import turtle

t = turtle.Turtle()
# We can change color and size of the pen
t.pensize(4)
t.pencolor("purple")

# color in the square
# colors are (r,g,b) where 1 is max
# purple -> (1,0,1)
# 
t.fillcolor("plum")
t.begin_fill()
t.forward(100)
t.right(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.end_fill()

#move to the next one
t.penup()
t.forward(200)
t.pendown()

#draw a triangle
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
