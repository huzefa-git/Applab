import turtle
import math

def draw_rectangle(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_polygon(num_sides, side_length):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(side_length)
        turtle.right(angle)

def draw_circle(radius):
    turtle.circle(radius)

def draw_sphere(radius):
    turtle.speed(1)  # Set a slower speed for better visibility
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Example usage:
turtle.speed(2)

# Draw a rectangle
draw_rectangle(100)

# Move to a new position
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

# Draw a triangle
draw_triangle(100)

# Move to a new position
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

# Draw a star
draw_star(100)

# Move to a new position
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()

# Draw a hexagon
draw_polygon(6, 70)

# Move to a new position
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

# Draw a circle
draw_circle(80)

# Move to a new position
turtle.penup()
turtle.goto(150, -150)
turtle.pendown()

# Draw a sphere
draw_sphere(50)

turtle.done()
