import turtle

def draw_pixel(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3, "black")  # Adjust dot size and color as needed

def bresenham_circle(x0, y0, radius):
    x = radius
    y = 0
    err = 0

    while x >= y:
        draw_pixel(x0 + x, y0 + y)
        draw_pixel(x0 + y, y0 + x)
        draw_pixel(x0 - y, y0 + x)
        draw_pixel(x0 - x, y0 + y)
        draw_pixel(x0 - x, y0 - y)
        draw_pixel(x0 - y, y0 - x)
        draw_pixel(x0 + y, y0 - x)
        draw_pixel(x0 + x, y0 - y)

        y += 1
        err += 1 + 2 * y

        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x

# Set up the turtle window
turtle.speed(-10)
turtle.hideturtle()
turtle.title("Bresenham's Circle Drawing Algorithm")

# Example usage
bresenham_circle(0, 0, 100)

# Close the turtle graphics window on click
turtle.exitonclick()
