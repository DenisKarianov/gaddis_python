# переводит арабские числа в римские

# запрашиваем число от 1 до 10 у пользователя
number = int(input('Введите целое число от 1 до 10: '))

# определяем категорию
if number == 1:
    print ('I')
elif number == 2:
    print ('II')
elif number == 3:
    print ('III')
elif number == 4:
    print ('IV')
elif number == 5:
    print ('V')
elif number == 6:
    print ('VI')
elif number == 7:
    print ('VII')
elif number == 8:
    print ('VIII')
elif number == 9:
    print ('IX')
elif number == 10:
    print ('X')
else:
    print ('Ошибка, введено неверное число. Нужно ввести целое число от 1 до 10.')