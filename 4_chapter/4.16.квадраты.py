# рисуем 100 квадратов

# именнованные константы
START_SQUARE_SIDE = 10 # размер стороны стартового квадрата
OFFSET = 5             # размер смещения
SQUARE_QUANTITY = 100  # количество квадратов

import turtle

# настраиваем черепаху и выводим на стартовую позицию
turtle.setup(600,600)
turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(290,-290)
turtle.pendown()

# задать размер стороны первого квадрата
square_side = START_SQUARE_SIDE

# рисуем первый квадрат
turtle.setheading (90)
for i in range (4):
    turtle.forward (square_side)
    turtle.left (90)

# рисуем остальные квадраты
for count in range (SQUARE_QUANTITY - 1):
    turtle.setheading (90)
    square_side += OFFSET
    for x in range (4):
        turtle.forward (square_side)
        turtle.left (90)