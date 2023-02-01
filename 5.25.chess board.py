# draw chess board

import turtle

# global constants
TURTLE_SPEED = 0
TURTLE_PENSIZE = 2
SQUARE_SIZE = 100
DARK_SQUARE_COLOR = 'black'
LIGHT_SQUARE_COLOR = 'white'


def main():
    turtle.hideturtle()
    turtle.speed(TURTLE_SPEED)
    turtle.pensize(TURTLE_PENSIZE)
    # draw 1, 3 and 5 raws
    y = 3.5 * SQUARE_SIZE
    for column in range(3):
        x = - (3.5 * SQUARE_SIZE)
        y -= 2 * SQUARE_SIZE
        for raw in range(1, 6):
            x += SQUARE_SIZE
            if raw % 2 == 0:
                square(x, y, SQUARE_SIZE, LIGHT_SQUARE_COLOR)
            else:
                square(x, y, SQUARE_SIZE, DARK_SQUARE_COLOR)
    # draw 2 and 4 raws
    y = 2.5 * SQUARE_SIZE
    for column in range(2):
        x = - (3.5 * SQUARE_SIZE)
        y -= 2 * SQUARE_SIZE
        for raw in range(1, 6):
            x += SQUARE_SIZE
            if raw % 2 == 0:
                square(x, y, SQUARE_SIZE, DARK_SQUARE_COLOR)
            else:
                square(x, y, SQUARE_SIZE, LIGHT_SQUARE_COLOR)

    turtle.done()  # to keep turtle's window up in pycharm


# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()  # Raise the pen
    turtle.goto(x, y)  # Move to the specified location
    turtle.fillcolor(color)  # Set the fill color
    turtle.pendown()  # Lower the pen
    turtle.begin_fill()  # Start filling
    for count in range(4):  # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()  # End filling


main()
