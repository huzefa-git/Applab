import turtle

def draw_heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50,200)
    turtle.right(140)
    turtle.circle(50,200)
    turtle.forward(133)
    turtle.end_fill()

turtle.speed(5)
turtle.pensize(2)

draw_heart()
turtle.penup()
turtle.goto(50,-50)


turtle.hideturtle()
turtle.done()