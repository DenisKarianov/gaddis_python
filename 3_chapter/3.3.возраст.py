# классификатор возраста

# запрашиваем возраст человека у пользователя
age = float(input('Укажите возраст человека: '))

# определяем категорию
if age <= 1:
    print ('Это младенец.')
elif age < 13:
    print ('Это ребёнок.')
elif age < 20:
    print ('Это подросток.')
else:
    print ('Это взрослый.')