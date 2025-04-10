from turtle import *


#we want to paint a house

#step 1: draw a square


width(5)

speed(10)
color("purple")
forward(200)

left(90)

forward(200)

left(90)

forward(200)

left(90)

forward(200)

left(90)

forward(70)

left(90)
color("yellow")
begin_fill()
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
left(120)
forward(50)
color("green")
begin_fill()
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
left(90)
forward(120)


exitonclick()