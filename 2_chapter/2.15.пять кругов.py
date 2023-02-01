# рисуем пять кругов, заходящих друг на друга

import turtle
turtle.setup (500, 500)
turtle.speed(5)
turtle.pensize(2)
turtle.penup()


# рисуем 1-й круг
turtle.goto(-100,0)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# рисуем 2-й круг
turtle.goto(10,0)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# рисуем 3-й круг
turtle.goto(120,0)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# рисуем 4-й круг
turtle.goto(-45,-50)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# рисуем 5-й круг
turtle.goto(65,-50)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

turtle.hideturtle()