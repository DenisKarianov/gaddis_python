# рисуем стороны света

import turtle
turtle.setup (500, 500)
turtle.speed(0)
turtle.pensize(2)
turtle.penup()


# линия запад-восток
turtle.goto(-100,0)
turtle.setheading(0)
turtle.pendown()
turtle.forward(200)
turtle.penup()

# линия север-юг
turtle.goto(0,100)
turtle.setheading(270)
turtle.pendown()
turtle.forward(200)
turtle.penup()

# круг
turtle.goto(0,-25)
turtle.setheading(0)
turtle.pendown()
turtle.circle(25)
turtle.penup()

# надпись север
turtle.goto(-15,100)
turtle.setheading(0)
turtle.pendown()
turtle.write('Север')
turtle.penup()

# надпись юг
turtle.goto(-5,-115)
turtle.setheading(0)
turtle.pendown()
turtle.write('Юг')
turtle.penup()

# надпись запад
turtle.goto(-135,-6)
turtle.setheading(0)
turtle.pendown()
turtle.write('Запад')
turtle.penup()

# надпись восток
turtle.goto(105,-6)
turtle.setheading(0)
turtle.pendown()
turtle.write('Восток')
turtle.penup()

turtle.hideturtle()