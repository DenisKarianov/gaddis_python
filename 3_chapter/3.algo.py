if x > 100:
    y = 20
	z = 40
	
if a < 10:
    b = 0
	c = 1
	
if a < 10:
    b = 0
else:
    b = 99
	
if score >= A_score:
    print ('Ваш уровень - А.')
else:
    if score >= B_score:
        print ('Ваш уровень - В.')
    else:
        if score >= C_score:
            print ('Ваш уровень - С.')
        else:
            if score >= D_score:
                print ('Ваш уровень - D.')
            else:
                print ('Ваш уровень - F.')
                
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print (amount1)
    else:
        if amount1 < amount2:
            print (amount2)
        else:
            print (f'Значения {amount1} и {amount2} равны.')
        
if speed >= 24 and speed <= 56:
    print ('Скорость нормальная')
else:
    print ('Скорость аварийная')
    
if points < 9 or points > 51:
    print ('Недопустимые точки')
else:
    print ('Допустимые точки')
    
import turtle
if turtle.heading() >= 0 and turtle.heading() <= 45:
    turtle.penup()

import turtle
if turtle.pencolor() == 'red' or turtle.pencolor() == 'blue':
    turtle.pensize(5)
    
import turtle
if turtle.xcor() >= 100 and turtle.xcor() <= 200 and turtle.ycor() >= 100 and turtle.ycor() <= 200:
    turtle.hideturtle()