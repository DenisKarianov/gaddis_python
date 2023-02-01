# Инструкции черепашьей графики по рисованию квадрата со стороной
# 100 пикселов и круг в центре квадрата радиусом 80 пикселов,
# заполненный красным цветом.
import turtle
turtle.setup(500, 500)
turtle.bgcolor('white')

#рисуем круг
turtle.penup()
turtle.home()
turtle.setheading(270) #направляю черепаху вниз, чтобы переместить черепаху
# и начать рисовать круг
turtle.forward(80) #перемещаю черепаху на начало рисования круга
# на расстояние, равное радиусу круга 80
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

#рисуем квадрат
turtle.penup()
turtle.home()
turtle.setheading(90) #устанавливаю направление черепахи наверх, чтобы
# переместить черепаху и начать рисовать квадрат с центром в точке (0, 0)
turtle.forward(50)
turtle.right(90)
turtle.pendown() #начинаю рисовать квадрат
turtle.fillcolor('white') # включаю заполнение квадрата белым цветом,
# чтобы он не был заполненным красным, как круг
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50) #закончили рисование квадрата
turtle.end_fill()

