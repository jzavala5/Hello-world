#Jose Zavala
#2/13/2020
#This is to make a polygon and fill the sides and length
#problem 3

sides=int(input("what is the number of sides of the polygon?"))

length=int(input("What is the length of the side?"))

colorline=input("Color of the line?")

colorfill=input("Fill color of a regular polygon?")

angle= 360/sides 

import turtle
wn = turtle.Screen()
polygon=turtle.Turtle()
polygon.color(colorline)
polygon.pensize(4)
polygon.fillcolor(colorfill)
polygon.begin_fill()

for i in range(sides):
    polygon.forward(length)
    polygon.left(angle)

##polygon.forward(75)
##polygon.left(90)
##polygon.forward(150)
##polygon.left(90)
##polygon.forward(75)
polygon.end_fill()
