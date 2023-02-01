# программа расчёта расходов на авто

def main():
    # запрос данных у пользователя
    credit_payment = float (input ("Введите ежемесячную сумму платежа по кредиту: "))
    insurance_payment = float (input ("Введите ежемесячную сумму платежа по страховке: "))
    fuel = float (input ("Введите ежемесячную расходы на топливо: "))
    oil = float (input ("Введите ежемесячную расходы на масло: "))
    tires = float (input ("Введите ежемесячные расходы на шины: "))
    service = float (input ("Введите ежемесячные расходы на тех.обслуживание: "))
    # вызов функции расчёта и показа расчётов
    show_expenses (credit_payment, insurance_payment, fuel, oil, tires, service) 
        
def split_number_spaces_and_make_commas(number):
    with_spaces = f'{number:,}'.format(number).replace(',', ' ')
    with_spaces_and_with_commas = f'{with_spaces}'.format(with_spaces).replace('.', ',')
    return with_spaces_and_with_commas

def show_expenses(credit_payment, insurance_payment, fuel, oil, tires, service):
    month_expenses = credit_payment + insurance_payment + fuel + oil + tires + service
    year_expenses = month_expenses * 12
    print (f'Ежемесячные расходы на авто: {split_number_spaces_and_make_commas(month_expenses)}')
    print (f'Ежегодные расходы на авто: {split_number_spaces_and_make_commas(year_expenses)}')

main()