import turtle
import random
from alphabet import alphabet
from math import cos, sin, atan2, radians, degrees

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)

window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message, fontSize, color, x, y, rotationAngle):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    myPen.write(message, move=False, align="left", font=("Arial", fontSize, "normal"))
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()

# Main Program Starts Here
fontSize = 30
fontColor = "#FF00FF"
characterSpacing = 5
cursorX = -150
cursorY = -100

message = "WordArt Challenge"

for char in message:
    charData = alphabet[char.upper()]
    displayMessage(char, fontSize, fontColor, cursorX, cursorY, charData[1])
    cursorX += charData[0] + characterSpacing

window.exitonclick()
