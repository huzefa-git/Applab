import turtle

def boundaryFill4(x, y, fill_color, boundary_color):
    if turtle.getpixel((x, y)) != boundary_color and turtle.getpixel((x, y)) != fill_color:
        turtle.pencolor(fill_color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(1)  # Draw a small line to fill the pixel

        # Recursively call the function for four neighboring points (right, left, above, below)
        boundaryFill4(x + 1, y, fill_color, boundary_color)  # Right
        boundaryFill4(x - 1, y, fill_color, boundary_color)  # Left
        boundaryFill4(x, y + 1, fill_color, boundary_color)  # Below
        boundaryFill4(x, y - 1, fill_color, boundary_color)  # Above

# Set up the turtle window
turtle.speed(0)
turtle.hideturtle()
turtle.title("4-connected Boundary Fill Algorithm")

# Draw a rectangle as a boundary
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)

# Call the boundary fill algorithm
boundaryFill4(100, 100, "red", "black")  # Assuming "red" is the fill color and "black" is the boundary color

# Close the turtle graphics window on click
turtle.exitonclick()
