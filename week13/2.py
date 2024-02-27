def drawLine(x1, y1, x2, y2):
    # Slope of the line (assuming x1 < x2 and y1 < y2)
    m = (y2 - y1) / (x2 - x1)

    # Initialize the starting point
    x, y = x1, y1

    # Draw the initial point
    print(x, y)

    while x < x2:
        x += 1
        y += m

        # Round the y-coordinate to the nearest integer
        rounded_y = round(y)

        # Write the code to print the intermediate point
        print(x, rounded_y)

# Examples
print("Example 1:")
drawLine(0, 0, 4, 4)

print("\nExample 2:")
drawLine(0, 0, 4, 2)
