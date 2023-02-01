# draw city silhouette

import turtle
import random

# global constants
TURTLE_SPEED = 0
TURTLE_PENSIZE = 1
BUILDINGS_COLOR = 'gray'
WINDOWS_COLOR = 'white'
SKY_COLOR = 'black'
STARS_COLOR = 'white'
STARS_SIZE = 2


def main():
    turtle.hideturtle()
    turtle.speed(TURTLE_SPEED)
    turtle.pensize(TURTLE_PENSIZE)
    draw_sky()
    draw_stars()
    draw_buildings()
    draw_windows()
    turtle.done()  # to keep turtle's window up in pycharm


# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def draw_buildings():
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(BUILDINGS_COLOR)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()

def draw_sky():
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(SKY_COLOR)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(210)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(200)
    turtle.end_fill()


# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling
    turtle.pensize(TURTLE_PENSIZE)

def draw_windows():
    turtle.setheading(0)
    square(-90, -25, 15, WINDOWS_COLOR)
    square(-40, 75, 15, WINDOWS_COLOR)
    square(-40, 50, 15, WINDOWS_COLOR)
    square(-5, 30, 15, WINDOWS_COLOR)
    square(-30, -65, 15, WINDOWS_COLOR)
    square(70, 20, 15, WINDOWS_COLOR)


def draw_stars():
    turtle.penup()
    for s in range(random.randint(50, 100)):
        turtle.goto(random.randint(-148, 148), random.randint(-148, 148))
        turtle.dot(STARS_SIZE, STARS_COLOR)


main()
