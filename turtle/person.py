import turtle

def draw_dream():
    window = turtle.Screen()
    window.bgcolor("white")
    draw_Scarlett()
    window.exitonclick()

def draw_Scarlett():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    draw_head(brad)
    draw_body(brad)
    draw_arm(brad)
    draw_leg1(brad)
    draw_leg2(brad)

def draw_head(brad):
    brad.circle(60)
    brad.speed(3)
    brad.right(60)

def draw_body(brad):
    num = 0
    while num < 3:
        brad.forward(150)
        brad.right(120)
        brad.speed(1)
        num += 1

def draw_arm(brad):
    brad.penup()
    brad.goto(40, 80)
    brad.pendown()
    brad.left(30)
    brad.forward(70)
    brad.right(90)
    brad.forward(30)
    brad.left(90)
    brad.forward(70)
    brad.right(90)
    brad.forward(30)

def draw_leg1(brad):
    brad.penup()
    brad.goto(-20, -70)
    brad.pendown()
    brad.left(60)
    brad.forward(80)
    brad.right(90)
    brad.forward(40)
    brad.left(90)
    brad.forward(80)
    brad.right(90)
    brad.forward(40)

def draw_leg2(brad):
    brad.penup()
    brad.goto(20, -70)
    brad.pendown()
    brad.left(120)
    brad.forward(80)
    brad.right(90)
    brad.forward(40)
    brad.left(90)
    brad.forward(80)
    brad.right(90)
    brad.forward(40)

if __name__ == "__main__":
    draw_dream()
