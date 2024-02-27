import turtle

def draw_spiral_helix(num_turns, circle_radius):
    for i in range(num_turns):
        turtle.circle(circle_radius * i)
        turtle.circle(-circle_radius * i)
        turtle.left(i)

def main():
    turtle.speed(10)
    num_turns = 100
    circle_radius = 5

    draw_spiral_helix(num_turns, circle_radius)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
