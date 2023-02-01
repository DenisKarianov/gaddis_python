# программа, которая превращает числа от 1 до 7 в дни недели

day_of_week = int(input('Пожалуйста, введите целое число от 1 до 7: '))

if day_of_week == 1:
    print ('понедельник')
elif day_of_week == 2:
    print ('вторник')
elif day_of_week == 3:
    print ('среда')
elif day_of_week == 4:
    print ('четверг')
elif day_of_week == 5:
    print ('пятница')
elif day_of_week == 6:
    print ('суббота')
elif day_of_week == 7:
    print ('воскресенье')
else:
    print ('введено неверное число')