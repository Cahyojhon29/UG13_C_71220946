import turtle 

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor('blue')
t.pencolor('cyan')
#angka 4
t.pensize(4.5)
t.left(90)
t.forward(70)
t.left(135)
t.forward(95)
t.left(135)
t.forward(67)
t.right(90)
t.forward(90)

#angka 9
t.penup()
t.goto(0,250)
t.pendown()
t.right(1)
t.penup()
t.forward(70)
t.pendown()
t.left(180)
t.forward(50)
t.circle(30,-360)
t.right(180)
t.forward(60)
t.circle(-30,180)
t.penup()

#angka 6
t.penup()
t.goto(-25,-175)
t.pendown()
t.circle(-30,180)
t.penup()
t.goto(-25,-175)
t.pendown()
t.forward(60)
t.left(180)
t.circle(-30,-360)
t.forward(50)
t.left(180)
t.pendown()
t.forward(70)
t.penup()
t.left(45)

#huruf c
t.penup()
t.goto(-200,0)
t.pendown()
t.circle(-45,-255)

#huruf j
t.penup()
t.goto(200,0)
t.pendown()
t.right(210)
t.forward(100)
t.right(90)
t.forward(100)
t.circle(-50,180)


s.exitonclick()