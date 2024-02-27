import turtle

def draw_rainbow_benzene():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')

    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)

def main():
    turtle.speed(-10)  # Set the turtle speed to the maximum
    draw_rainbow_benzene()
    turtle.exitonclick()

if __name__ == "__main__":
    main()
