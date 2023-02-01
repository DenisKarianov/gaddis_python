# программа расчёта стоимости страховки

# глобальные константы
INSURANCE_RATE = 0.8

def main():
    # ввод стоимости строения
    price = float (input ("Введите стоимость строения и нажмите 'Enter': "))
    # вызов функции расчёта страховой суммы и присвоения результата переменной
    insurance = count_insurance(price)
    # вывод на печать минимальной страховой суммы
    print (f'Минимальная страховая сумма: {insurance}')
    
def return_split_number_spaces(number):
    return f'{number:,}'.format(number).replace(',', ' ')

def count_insurance(price):
    insurance = return_split_number_spaces(price * INSURANCE_RATE)
    return insurance

main()