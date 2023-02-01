# считаем бюджет

# запрашиваем у пользователя сумму его бюджета на месяц
budget = float (input ('Введите выделенную на месяц сумму в евро: '))

# запрашиваем у пользователя количество статей расходов
quantity = int (input ('Введите количество статей расходов: '))

# объявляем накопитель для потраченной суммы
total = 0

# запрашиваем у пользователя суммы потраченных статей расходов
for x in range (quantity):
    sum = float (input ('Введите потраченную на конкретную статью расходов сумму в евро: '))
    total += sum

#сравниваем потраченную сумму и бюджет и выводим результат
if budget > total:
    print (f'Вы сэкономили {budget - total} евро.')
elif budget < total:
    print (f'Вы излишне потратили {total - budget} евро.')
else:
    print ('Вы потратили всю выделенную на месяц сумму.')