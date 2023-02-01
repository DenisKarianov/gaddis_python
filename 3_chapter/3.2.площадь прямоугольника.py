# программа, которая сравнивает площадь двух прямоугольников

# запрашиваем длину и ширину прямоугольников у пользователя
rectangle_1_length = float(input('Введите длину 1-го прямоугольника: '))
rectangle_1_width = float(input('Введите ширину 1-го прямоугольника: '))
rectangle_2_length = float(input('Введите длину 2-го прямоугольника: '))
rectangle_2_width = float(input('Введите ширину 2-го прямоугольника: '))

# считаем площади, сравниваем и выводим на печать ту, что больше,
# или сообщение о том, что площади равны
if rectangle_1_length*rectangle_1_width > rectangle_2_length*rectangle_2_width:
    print ('Площадь первого прямоугольника больше.')
elif rectangle_1_length*rectangle_1_width < rectangle_2_length*rectangle_2_width:
    print ('Площадь второго прямоугольника больше.')
else:
    print ('Площадь прямоугольников равна.')