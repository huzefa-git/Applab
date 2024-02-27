import turtle
from math import pi

from time import sleep

window = turtle.Screen()
window.bgcolor("black")
window.tracer(0)  # Use tracer on the Screen, not on the Turtle

mypen = turtle.Turtle()
mypen.hideturtle()
mypen.speed(0)
mypen.pensize(3)
mypen.color("white")
mypen.penup()

radius = 4
for i in range(0, 1000):
    area = pi * radius**2  # Corrected the formula for the area of a circle
    mypen.circle(radius)
    mypen.pendown()

    # Removed the problematic "mypen.clear()" line

    # Update the screen
    window.update()
    sleep(0.05)  # Adjust the sleep duration to control the animation speed

window.mainloop()
