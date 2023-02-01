# рассчитываем рост платы за обучение

# объявляем переменную стоимости обучения в текущем году
year_payment = 145000

# объявляем постоянную переменную процент ежегодного увеличения платы
YEAR_RAISE_PERCENT = 3

# объявляем постоянную переменную количества лет для расчёта
YEAR_QUANTITY = 5

# считаем и выводим стоимость обучения за каждый год
for year in range (YEAR_QUANTITY):
    year_payment += year_payment/100*YEAR_RAISE_PERCENT
    if year + 1 == 1:
        print (f'Через {year + 1} год стоимость обучения составит {year_payment:.2f} рублей.')
    elif year + 1 == 2 or year + 1 == 3 or year + 1 == 4:
        print (f'Через {year + 1} года стоимость обучения составит {year_payment:.2f} рублей.')
    else:
        print (f'Через {year + 1} лет стоимость обучения составит {year_payment:.2f} рублей.')