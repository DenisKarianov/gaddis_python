# расчёт размера скидки за опт

# запрашиваем у пользователя количество приобретённых пакетов ПО
quantity = int (input('Введите количество приобретённых пакетов ПО: '))

# считаем скидку и выводим информацию
if quantity < 10:
    print ('Скидка отсутствует.')
elif quantity >= 10 and quantity <= 19:
    discount = quantity*99/100*10
    print (f'Ваша скидка составляет {discount:.2f} рублей.')
    print (f'Общая сумма покупки с учётом скидки составляет {quantity*99 - discount:.2f} рублей.')
elif quantity >= 20 and quantity <= 49:
    discount = quantity*99/100*20
    print (f'Ваша скидка составляет {discount:.2f} рублей.')
    print (f'Общая сумма покупки с учётом скидки составляет {quantity*99 - discount:.2f} рублей.')
elif quantity >= 50 and quantity <= 99:
    discount = quantity*99/100*30
    print (f'Ваша скидка составляет {discount:.2f} рублей.')
    print (f'Общая сумма покупки с учётом скидки составляет {quantity*99 - discount:.2f} рублей.')
elif quantity >= 100:
    discount = quantity*99/100*40
    print (f'Ваша скидка составляет {discount:.2f} рублей.')
    print (f'Общая сумма покупки с учётом скидки составляет {quantity*99 - discount:.2f} рублей.')
else:
    print ('Ошибка. Пожалуйста, проверьте введённое число купленных пакетов ПО.')