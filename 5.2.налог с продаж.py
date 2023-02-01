# программа расчёта налога с продаж

# глобальные константы
FED_SALE_TAX_RATE = 0.05
REG_SALE_TAX_RATE = 0.025

def main():
    # ввод суммы покупки
    sale_sum = float (input ("Введите сумму покупки и нажмите 'Enter': "))
    fed_sale_tax, reg_sale_tax = sale_tax(sale_sum)
    # вывод на печать суммы покупки, федеральный налог с продаж, регио­
    # нальный налог с продаж, общий налог с продаж и общую сумму продажи
    print (f'Сумма покупки: {sale_sum}')
    print (f'Федеральный налог с продаж: {fed_sale_tax}')
    print (f'Региональный налог с продаж: {reg_sale_tax}')
    print (f'Общий размер налога с продаж: {fed_sale_tax + reg_sale_tax}')
    print (f'Общая сумма продажи: {sale_sum + fed_sale_tax + reg_sale_tax}')

def sale_tax(sale_sum):
    fed_sale_tax = sale_sum * FED_SALE_TAX_RATE
    reg_sale_tax = sale_sum * REG_SALE_TAX_RATE
    return fed_sale_tax, reg_sale_tax

main()