# turtle graphic, function for triangle
import turtle

# global constants
X1 = 100
Y1 = 100
X2 = 50
Y2 = 0
X3 = -10
Y3 = 10
COLOR = 'yellow'


def main():
    triangle(X1, Y1, X2, Y2, X3, Y3, COLOR)
    turtle.done() # to keep turtle's window up in pycharm


# function to draw triangle with x and y coordinates of dots and fill color
def triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()


main()
