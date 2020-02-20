#Jose Zavala
#2/13/2020
#This program help us become better with the tutle function.

import turtle
wn = turtle.Screen()
wn.bgcolor("purple")

pokeball = turtle.Turtle()
pokeball.color("black")
pokeball.pensize(10)

button = turtle.Turtle()

pokeball.circle(50)
#pokeball.getscreen()._root.mainloop()
button.penup()
button.pensize(10)
button.left(90)
button.forward(50)
button.pendown()
button.left(90)
button.forward(50)
button.right(180)
button.forward(100)
#button.left(50)
button.penup()
button.goto(0,40)
button.pendown()
button.circle(10)
