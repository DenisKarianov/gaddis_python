# программа расчёта налога на недвижимость

# глобальные константы
TAX_RATE = 0.0072  # ставка налога
REALTY_RATE = 0.6  # коэффициент конвертации в оценочную стоимость
DECIMAL_PLACES = 2 # количество знаков в десятичной дробив (после запятой)

def main():
    # запрос данных у пользователя
    actual_cost = float (input ("Введите фактическую стоимость недвижимости в $: "))
    # вызов функции расчёта и показа оценочной стоимости и налога
    show_taxes(actual_cost) 
        
def split_number_spaces_and_make_commas(number, quantity):
    if quantity != 0:
        if quantity == 1:
            with_spaces = f'{number:,.1f}'.format(number).replace(',', ' ')
        elif quantity == 2:
            with_spaces = f'{number:,.2f}'.format(number).replace(',', ' ')
        else:
            with_spaces = f'{number:,.2f}'.format(number).replace(',', ' ')
    else:
        with_spaces = f'{number:,}'.format(number).replace(',', ' ')
    with_spaces_and_with_commas = f'{with_spaces}'.format(with_spaces).replace('.', ',')
    return with_spaces_and_with_commas

def show_taxes(actual_cost):
    assessed_value = actual_cost * REALTY_RATE
    tax = assessed_value * TAX_RATE
    print (f'Оценочная стоимость недвижимости: ${split_number_spaces_and_make_commas(assessed_value, DECIMAL_PLACES)}')
    print (f'Налог на недвижимость: ${split_number_spaces_and_make_commas(tax, DECIMAL_PLACES)}')
    
main()