# смешение цветов

# запрашиваем два основных цвета у пользователя
color1 = input('Введите желтый, синий или красный цвет: ')
color2 = input('Введите желтый, синий или красный цвет: ')

# проверяем смешение цветов и сообщаем
if color1 == 'желтый' and color2 == 'красный':
    print (f'Если смешать {color1} и {color2}, получится оранжевый.')
elif color2 == 'желтый' and color1 == 'красный':
    print (f'Если смешать {color1} и {color2}, получится оранжевый.')
elif color1 == 'жёлтый' and color2 == 'красный':
    print (f'Если смешать {color1} и {color2}, получится оранжевый.')
elif color2 == 'жёлтый' and color1 == 'красный':
    print (f'Если смешать {color1} и {color2}, получится оранжевый.')
elif color1 == 'желтый' and color2 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится зелёный.')
elif color2 == 'желтый' and color1 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится зелёный.')
elif color1 == 'жёлтый' and color2 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится зелёный.')
elif color2 == 'жёлтый' and color1 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится зелёный.')
elif color1 == 'красный' and color2 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится фиолетовый.')
elif color2 == 'красный' and color1 == 'синий':
    print (f'Если смешать {color1} и {color2}, получится фиолетовый.')
elif color1 == color2:
    print (f'Если смешать {color1} и {color2}, получится {color1}.')
elif color1 == 'желтый' and color2 == 'жёлтый':
    print (f'Если смешать {color1} и {color2}, получится жёлтый.')
elif color2 == 'желтый' and color1 == 'жёлтый':
    print (f'Если смешать {color1} и {color2}, получится жёлтый.')
else:
    print ('Ошибка, введены неверные цвета.')