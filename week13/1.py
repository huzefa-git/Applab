import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA Line Drawing")

# Define colors
WHITE = (255, 255, 255)

def draw_line_dda(X0, Y0, X1, Y1):
    # Calculate dx, dy
    dx = X1 - X0
    dy = Y1 - Y0

    # Depending upon absolute value of dx & dy,
    # choose number of steps to put pixel
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate increments for x and y
    Xinc = dx / float(steps)
    Yinc = dy / float(steps)

    # Initialize starting point
    X, Y = X0, Y0

    # Draw the line
    for _ in range(steps + 1):
        pygame.draw.rect(screen, WHITE, (round(X), round(Y), 1, 1))  # Draw a pixel at (X, Y)
        X += Xinc
        Y += Yinc
        pygame.display.flip()  # Update the display

# Example 1
draw_line_dda(50, 50, 200, 200)

# Example 2
draw_line_dda(100, 100, 100, 300)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
