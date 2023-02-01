# draw snowman
import turtle

# global constants
RADIUS = 100  # radius of base snowball
TURTLE_SPEED = 5
HAT_COLOR = 'black'


def main():
    turtle.speed(TURTLE_SPEED)
    turtle.pensize(2)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    turtle.done()  # to keep turtle's window up in pycharm


# function to draw triangle with x and y coordinates of dots and fill color
def drawBase():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 0 - 2 * RADIUS)
    turtle.pendown()
    turtle.circle(RADIUS)
    turtle.penup()


def drawMidSection():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(RADIUS - RADIUS * 0.3)
    turtle.penup()


def drawArms():
    turtle.hideturtle()
    # draw right arm
    turtle.penup()
    turtle.goto(0, RADIUS - RADIUS * 0.3)  # go to center of mid snowball
    turtle.setheading(10)
    turtle.forward(RADIUS - RADIUS * 0.3)  # go to circle
    turtle.pendown()
    turtle.setheading(40)
    turtle.forward(RADIUS - RADIUS * 0.2)  # draw right arm
    turtle.setheading(80)
    turtle.forward(RADIUS * 0.2)  # draw upper finger of right arm
    turtle.penup()
    turtle.backward(RADIUS * 0.2)
    turtle.pendown()
    turtle.right(80)
    turtle.forward(RADIUS * 0.2)  # draw lower finger of right arm
    # draw left arm
    turtle.penup()
    turtle.goto(0, RADIUS - RADIUS * 0.3)  # go to center of mid snowball
    turtle.setheading(170)
    turtle.forward(RADIUS - RADIUS * 0.3)  # go to circle
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward((RADIUS - RADIUS * 0.2) / 2)  # draw 1st part of left arm
    turtle.right(50)
    turtle.forward((RADIUS - RADIUS * 0.2) / 2)  # draw 2nd part of left arm
    turtle.right(40)
    turtle.forward(RADIUS * 0.2)  # draw upper finger of left arm
    turtle.penup()
    turtle.backward(RADIUS * 0.2)
    turtle.pendown()
    turtle.left(80)
    turtle.forward(RADIUS * 0.2)  # draw lower finger of left arm
    turtle.penup()


def drawHead():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 2 * (RADIUS - RADIUS * 0.3))  # go to most upper part of mid snowball
    turtle.pendown()
    turtle.setheading(0)
    mid_radius = RADIUS - RADIUS * 0.3
    turtle.circle(mid_radius - mid_radius * 0.3)  # draw head
    # draw right eye
    turtle.penup()
    turtle.goto(0, 2 * (RADIUS - RADIUS * 0.3) + (mid_radius - mid_radius * 0.3))  # go to center of head snowball
    turtle.setheading(45)
    turtle.forward((mid_radius - mid_radius * 0.3) / 2.4)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(mid_radius * 0.07)
    turtle.penup()
    # draw left eye
    turtle.goto(0, 2 * (RADIUS - RADIUS * 0.3) + (mid_radius - mid_radius * 0.3))  # go to center of head snowball
    turtle.setheading(135)
    turtle.forward((mid_radius - mid_radius * 0.3) / 2.4)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(mid_radius * 0.07)
    turtle.penup()
    # draw mouth
    turtle.goto(-((mid_radius - mid_radius * 0.3) / 2),
                2 * (RADIUS - RADIUS * 0.3) + (mid_radius - mid_radius * 0.3) * 0.8)  # go to beginning of the mouth
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(mid_radius - mid_radius * 0.3)
    turtle.penup()


def drawHat():
    turtle.hideturtle()
    turtle.penup()
    mid_radius = RADIUS - RADIUS * 0.3
    small_radius = (RADIUS - RADIUS * 0.3) - (RADIUS - RADIUS * 0.3) * 0.3
    turtle.goto(- (1.2 * small_radius),
                2 * (RADIUS - RADIUS * 0.3) + (mid_radius - mid_radius * 0.3) + ((mid_radius - mid_radius * 0.3) / 1.6))
    turtle.setheading(0)
    turtle.fillcolor(HAT_COLOR)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(2.4 * small_radius)
    turtle.left(90)
    turtle.forward(0.4 * small_radius)
    turtle.left(90)
    turtle.forward(0.6 * small_radius)
    turtle.right(90)
    turtle.forward(small_radius)
    turtle.left(90)
    turtle.forward(1.2 * small_radius)
    turtle.left(90)
    turtle.forward(small_radius)
    turtle.right(90)
    turtle.forward(0.6 * small_radius)
    turtle.left(90)
    turtle.forward(0.4 * small_radius)
    turtle.end_fill()


main()
