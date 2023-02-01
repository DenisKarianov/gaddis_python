# Эта программа наносит звёзды созвездия Ориона,
# названия звёзд и линии созвездия.
import turtle

# Задать размер окна.
turtle.setup(500, 600)

# Установить черепаху.
turtle.penup()
turtle.hideturtle()

# Создать именнованные константы для звёздных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_Х = 80
RIGHT_SHOULDER_У = 180

LEFT_BELTSTAR_Х = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_Х = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_Х = 40
RIGHT_BELTSTAR_Y = 20

LEFT_КNЕЕ_Х = -90
LEFT_КNЕЕ_Y = -180

RIGHT_КNЕЕ_X = 120
RIGHT_КNЕЕ_Y = -140

# Нанести звёзды
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо
turtle.dot()
turtle.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_У) # Правое плечо
turtle.dot()
turtle.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y) # Левая звезда в поясе
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y) # Средняя звезда в поясе
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y) # Правая звезда в поясе
turtle.dot()
turtle.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y) # Левая звезда в колене
turtle.dot()
turtle.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y) # Правая звезда в колене
turtle.dot()

# Вывести названия звёзд
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_У) # Правое плечо
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y) # Левая звезда в поясе
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y) # Средняя звезда в поясе
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y) # Правая звезда в поясе
turtle.write('Минтака')
turtle.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y) # Левая звезда в колене
turtle.write('Саиф')
turtle.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y) # Правая звезда в колене
turtle.write('Ригель')

# Нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_Х, RIGHT_SHOULDER_У)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELTSTAR_Х, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в левую звезду колена
turtle.goto(LEFT_BELTSTAR_Х, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_КNЕЕ_Х, LEFT_КNЕЕ_Y)
turtle.penup()

# Нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_Х, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y)
turtle.penup()

# Оставить окно открытым.
turtle.done()