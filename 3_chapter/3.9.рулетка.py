# определяем цвет кармана рулетки

# просим пользователя ввести номер кармана рулетки от 0 до 36 включительно
number = int(input('Введите номер кармана рулетки от 0 до 36, включительно: '))

# определяем цвет кармана и выводит соответствующее сообщение
if number == 0:
    print ('Цвет кармана рулетки - зелёный.')
elif number >= 1 and number <= 10:
    if number%2 != 0:
        print ('Цвет кармана рулетки - красный.')
    else:
        print ('Цвет кармана рулетки - чёрный.')
elif number >= 11 and number <= 18:
    if number%2 != 0:
        print ('Цвет кармана рулетки - чёрный.')
    else:
        print ('Цвет кармана рулетки - красный.')
elif number >= 19 and number <= 28:
    if number%2 != 0:
        print ('Цвет кармана рулетки - красный.')
    else:
        print ('Цвет кармана рулетки - чёрный.')
elif number >= 29 and number <= 36:
    if number%2 != 0:
        print ('Цвет кармана рулетки - чёрный.')
    else:
        print ('Цвет кармана рулетки - красный.')
else:
    print ('Ошибка, введён неверный номер кармана. Номер должен быть от 0 до 36, включительно.')