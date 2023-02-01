# рисуем гипнотический узор

# именнованные константы
START_LINE_LENGTH = 0     # длина линии
OFFSET = 7   # увеличение длины линии
LINE_QUANTITY = 49  # количество линий

import turtle

# настраиваем черепаху и выводим на стартовую позицию
turtle.setup(600,600)
turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(0,0)
turtle.setheading (90)
turtle.pendown()

# объявляем переменную длины линии
line_length = START_LINE_LENGTH

# рисуем узор
for count in range (LINE_QUANTITY):
    line_length += OFFSET
    turtle.forward(line_length)
    turtle.left(90)