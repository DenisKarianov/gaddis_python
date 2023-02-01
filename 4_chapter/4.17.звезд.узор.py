# рисуем звездочный узор

# именнованные константы
LINE_LENGTH = 150     # длина линии
OFFSET_ANGLE = 135   # угол смещения
LINE_QUANTITY = 100  # количество линий

import turtle

# настраиваем черепаху и выводим на стартовую позицию
turtle.setup(600,600)
turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(0,0)
turtle.setheading (0)
turtle.pendown()

# рисуем узор
for count in range (LINE_QUANTITY):
    turtle.forward(LINE_LENGTH)
    turtle.left(OFFSET_ANGLE)