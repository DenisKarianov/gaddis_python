# программа определяет количество дней в феврале в определенном году

# запрашиваем у пользователя год
year = int (input('Введите год (4 цифры): '))

# преобразуем и выводим информацию
if year%100 == 0 and year%400 == 0:
    print (f'В {year} году в феврале 29 дней.')
else:
    if year%4 == 0:
        print (f'В {year} году в феврале 29 дней.')
    else:
        print (f'В {year} году в феврале 28 дней.')