import turtle

# Set up the turtle
turtle.speed(2)
turtle.pensize(2)

# Draw the head
turtle.circle(100)

# Draw the left eye
turtle.penup()
turtle.goto(-40, 120)
turtle.pendown()
turtle.circle(15)

# Draw the right eye
turtle.penup()
turtle.goto(40, 120)
turtle.pendown()
turtle.circle(15)

# Draw the mouth
turtle.penup()
turtle.goto(-40, 85)
turtle.pendown()
turtle.right(90)
turtle.circle(40, 180)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
