# рисуем 8-угольный знак stop

# именнованные константы
SIDE_LENGTH = 100     # длина стороны 8-угольника
OFFSET = 10           # смещение текста

#считаем радиус писанной окружности и объявляем соответствующую переменную
radius = SIDE_LENGTH * (2 ** 0.5 + 1) / 2

import turtle

# настраиваем черепаху и выводим на стартовую позицию
turtle.setup(500,500)
turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(-radius,-radius)
turtle.setheading (0)
turtle.pendown()

# рисуем 8-угольник
for count in range (8):
    turtle.forward(SIDE_LENGTH)
    turtle.left(45)

#переходим в центр 8-угольника и пишем стоп
turtle.penup()
turtle.setheading (0)
turtle.forward(SIDE_LENGTH / 2)
turtle.left(90)
turtle.forward(radius - OFFSET)
turtle.pendown()
turtle.write('STOP', align='center', font=("Verdana", 12, "normal"))
