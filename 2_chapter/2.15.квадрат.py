# рисуем хитрый квадрат

import turtle
turtle.setup (500, 500)
turtle.speed(0)
turtle.pensize(1)
turtle.penup()

# рисуем квадрат по периметру и точки
turtle.goto(-100,100)
turtle.setheading(270)
turtle.pendown()
turtle.dot()
turtle.forward(200)
turtle.dot()
turtle.left(90)
# прерывистая линия
turtle.forward(20)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(20)

turtle.dot()
turtle.left(90)
turtle.forward(200)
turtle.dot()
turtle.left(90)
# вторая прерывистая линия
turtle.forward(20)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(20)

# диагональ из левого верхнего угла в правый нижний с точкой посередине
turtle.goto(0,0)
turtle.dot()
turtle.goto(100,-100)

# диагональ из правого верхнего угла в левый нижний
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(-100,-100)

turtle.hideturtle()