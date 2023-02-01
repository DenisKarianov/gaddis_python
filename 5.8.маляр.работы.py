# программа оценки стоимости малярных работ

# глобальные константы
WORK_NECESSARY_10_SQM = 8
WORK_PRICE_1HOUR = 2000


def main():
    # запрос данных у пользователя
    wall_square = float(input("Введите площадь стены под покраску в кв.м: "))
    paint_5_litres_price = float(input("Введите стоимость 5-литровой ёмкости краски: "))

    # вызов функции расчёта и показа данных
    show_expenses(wall_square, paint_5_litres_price)


def show_expenses(square, paint_price):
    # считаем необходимое количество упаковок краски
    if square % 10 != 0:
        paint_can_quantity = int (square // 10 + 1)
    else:
        paint_can_quantity = int (square // 10)

    # считаем необходимое количество рабочих часов
    if square % 10 != 0:
        work_hour_necessary_all = int (square // (10 / WORK_NECESSARY_10_SQM) + 1)
    else:
        work_hour_necessary_all = int (square // (10 / WORK_NECESSARY_10_SQM))

    # считаем стоимость работ
    work_price_all = work_hour_necessary_all * WORK_PRICE_1HOUR

    # считаем стоимость работ и краски
    work_and_paint_price_all = work_price_all + paint_price * paint_can_quantity

    # вывод данных на экран
    print(f'Для покраски {square} квадратных метров стены:')
    print(f'Требуется пятилитровых ёмкостей краски: {paint_can_quantity}.')
    print(f'Требуется {work_hour_necessary_all} рабочих часов.')
    print(f'Стоимость 5-литровой ёмкости краски - {paint_price} рублей.')
    print(f'Стоимость работ по покраске: {work_price_all} рублей.')
    print(f'Стоимость работ по покраске вместе со стоимостью краски: {work_and_paint_price_all} рублей.')


main()
