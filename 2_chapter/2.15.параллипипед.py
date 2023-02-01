# рисуем параллелипипед

import turtle
turtle.setup (500, 500)

# рисуем первый квадрат
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

# нижняя косая черта
turtle.goto(50,-50)
turtle.setheading(0)

# рисуем второй квадрат
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

# верхняя косая черта
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.goto(100,0)

# средняя косая черта
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.goto(100,-50)

turtle.hideturtle()