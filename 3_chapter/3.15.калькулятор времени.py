# программа преобразует секунды в большие единицы времени

# запрашиваем у пользователя количество секунд
sec = int (input('Введите количество секунд: '))

# преобразуем и выводим информацию
if sec >= 60 and sec < 3600:
    print (f'{sec} секунд составляют {sec//60} минут и {sec%60} секунд.')
elif sec >= 3600 and sec < 86400:
    print (f'{sec} секунд составляют {sec//3600} часов, {sec%3600//60} минут и {sec%3600%60} секунд.')
elif sec >= 86400:
    print (f'{sec} секунд составляют {sec//86400} дней, {sec%86400//3600} часов, {sec%86400%3600//60} минут и {sec%86400%3600%60} секунд.')
else:
    print ('Ошибка. Пожалуйста, число секунд, равное 60 или больше.')