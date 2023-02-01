# таблица градусов по цельсию и фаренгейту от 0 до 20 по цельсию

# выводим названия столбцов и разделительную полосу
celsuis_name = 'Градусов Цельсия'
farenheit_name = 'Градусов Фаренгейта'
print (f'{celsuis_name:^21}', end='')
print (f'{farenheit_name:^21}')
print ('-------------------------------------------')

# выводим градусы
for celsius in range (21):
    farenheit = 9 * celsius / 5 + 32
    print (f'{celsius:^21}{farenheit:^21}')