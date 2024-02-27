import turtle
import time
from random import randint

# Change this value to speed up or slow down this animation
animationSpeed = 2
gridSize = 15
myPen = turtle.Turtle()
myPen.shape("turtle")
myPen._tracer(0)
myPen.speed(0)
myPen.color("#000000")
topLeft_x = -180
topLeft_y = 180

# Draw the grid on screen (intDim is the width of a cell on the grid)
def drawGrid(grid, intDim):
    myPen.penup()
    myPen.goto(topLeft_x, topLeft_y)

    for row in grid:
        for col in row:
            if col == 1:
                myPen.color("#000000")  # Set color for grid cell (black)
            else:
                myPen.color("#FFFFFF")  # Set color for grid cell (white)

            myPen.pendown()
            myPen.begin_fill()

            # Draw rectangle for the grid cell
            for _ in range(4):
                myPen.forward(intDim)
                myPen.right(90)

            myPen.end_fill()
            myPen.penup()
            myPen.forward(intDim)

        myPen.backward(gridSize * intDim)
        myPen.right(90)
        myPen.forward(intDim)
        myPen.left(90)

    myPen.hideturtle()


# Example usage:
# Create a sample grid (you may replace this with your actual grid)
sampleGrid = [[0] * gridSize for _ in range(gridSize)]
for i in range(gridSize):
    for j in range(gridSize):
        sampleGrid[i][j] = randint(0, 1)

# Set the dimension of a cell on the grid
cellWidth = 20

# Draw the grid
drawGrid(sampleGrid, cellWidth)

# Display the grid for a few seconds
time.sleep(5)
turtle.done()
