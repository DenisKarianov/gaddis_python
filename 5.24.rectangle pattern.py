# draw rectangle pattern

import turtle

# global constants
TURTLE_SPEED = 5
TURTLE_PENSIZE = 2
INNER_RECTANGLE_COLOR = 'black'


def main():
    turtle.speed(TURTLE_SPEED)
    turtle.pensize(TURTLE_PENSIZE)
    width = int(input('Enter width of pattern in pixels: '))
    height = int(input('Enter height of pattern in pixels: '))
    drawPattern(width, height)
    turtle.done()  # to keep turtle's window up in pycharm


def drawPattern(width, height):
    turtle.hideturtle()
    # draw outer rectangle
    turtle.penup()
    turtle.goto(- (width / 2), height / 2)  # go to left upper angle of outer rectanlge
    turtle.pendown()
    turtle.setheading(0)
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    # draw middle rectangle
    turtle.penup()
    turtle.goto(- (width * 0.8 / 2), height * 0.8 / 2)  # go to left upper angle of middle rectangle
    turtle.pendown()
    turtle.setheading(0)
    for i in range(2):
        turtle.forward(width * 0.8)
        turtle.right(90)
        turtle.forward(height * 0.8)
        turtle.right(90)
    # draw inner rectangle
    turtle.penup()
    turtle.goto(- (width * 0.6 / 2), height * 0.6 / 2)  # go to left upper angle of inner rectangle
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor(INNER_RECTANGLE_COLOR)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width * 0.6)
        turtle.right(90)
        turtle.forward(height * 0.6)
        turtle.right(90)
    turtle.end_fill()
    # draw diagonals
    turtle.penup()
    turtle.goto(- (width / 2), height / 2)  # go to left upper angle of outer rectanlge
    turtle.pendown()
    turtle.goto(width / 2, - (height / 2))  # draw 1st diagonal
    turtle.penup()
    turtle.goto(width / 2, height / 2)  # go to right upper angle of outer rectanlge
    turtle.pendown()
    turtle.goto(- (width / 2), - (height / 2))  # draw 2nd diagonal
    # draw perpendicular lines
    turtle.penup()
    turtle.goto(0, height / 2)  # go to the middle of upper line of outer rectanlge
    turtle.pendown()
    turtle.goto(0, - (height / 2))  # draw vertical line
    turtle.penup()
    turtle.goto(- (width / 2), 0)  # go to the middle of left line of outer rectanlge
    turtle.pendown()
    turtle.goto(width / 2, 0)  # draw horizontal line


main()
