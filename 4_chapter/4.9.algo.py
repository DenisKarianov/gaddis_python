number = float (input ('Введите число от 1 до 100: '))
while number < 1 or number > 100:
    print ('Ошибка, введено неверное число!')
    number = float (input ('Введите число от 1 до 100: '))
print ('Вы ввели правильное число!')
