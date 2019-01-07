# Python 3.7.1
import turtle

turtle.hideturtle()
turtle.speed(speed=10)


for i in range(60):
    turtle.color('black')
    turtle.circle(20)
    turtle.circle(50)
    turtle.circle(35)
    turtle.circle(40)
    turtle.circle(25*i)
    turtle.circle(-25*i)
  

turtle.end_fill()
turtle.done()
