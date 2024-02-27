import turtle
import random
from alphabet import alphabet
from time import sleep

myPen = turtle.Turtle()
myPen.hideturtle()
myPen._tracer(0)
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(4)

def draw_letter(letter, fontSize, color, x, y):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    myPen.write(letter, align="center", font=("Arial", fontSize, "normal"))

def morphing(letter1, letter2, t, fontSize, color, x, y):
    for i in range(26):
        intermediate_letter = ""
        for j in range(len(letter1)):
            char1 = letter1[j]
            char2 = letter2[j]
            intermediate_char = chr(int(ord(char1) + (ord(char2) - ord(char1)) * t))
            intermediate_letter += intermediate_char

        draw_letter(intermediate_letter, fontSize, color, x, y)
        myPen.clear()

        t += 1 / 26
        myPen._update()
        sleep(0.1)

# Example usage
morphing("HELLO", "WORLD", 0, 36, "white", 0, 0)

turtle.done()
