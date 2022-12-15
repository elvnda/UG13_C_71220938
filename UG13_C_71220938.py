import turtle

s = turtle.Screen()
s.bgcolor('pink')
t = turtle.Turtle()
t.pencolor('black')
t.pensize(10)

#I
t.penup()
t.goto(-200,100)
t.pendown()
t.right(90)
t.forward(180)

#H
t.penup()
t.goto(200,100)
t.pendown()
t.forward(180)
t.back(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.back(180)


#3

t.penup()
t.goto(-90,-80)
t.pendown()
t.right(90)
t.forward(100)

t.left(90)
t.forward(90)
t.left(90)
t.forward(100)
t.left(180)
t.forward(100)
t.left(90)
t.forward(90)
t.left(90)
t.forward(100)


#3
t.penup()
t.goto(-90,250)
t.pendown()
t.circle(35,350)
t.circle(35,270)
t.backward(90)




s.exitonclick()


