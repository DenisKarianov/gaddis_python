# программа расчёта дохода от продажи билетов

# глобальные константы
A_TICKET_PRICE = 20
B_TICKET_PRICE = 15
C_TICKET_PRICE = 10

def main():
    # запрос данных у пользователя
    a_ticket_quantity = int (input ("Введите количество проданных билетов класса А: "))
    b_ticket_quantity = int (input ("Введите количество проданных билетов класса B: "))
    c_ticket_quantity = int (input ("Введите количество проданных билетов класса C: "))
    # вызов функции расчёта и показа дохода
    show_income(a_ticket_quantity, b_ticket_quantity, c_ticket_quantity) 
        
def show_income(a_ticket_quantity, b_ticket_quantity, c_ticket_quantity):
    a_ticket_income = a_ticket_quantity * A_TICKET_PRICE
    b_ticket_income = b_ticket_quantity * B_TICKET_PRICE
    c_ticket_income = c_ticket_quantity * C_TICKET_PRICE
    print (f'Доход от продажи билетов: ${a_ticket_income + b_ticket_income + c_ticket_income}.')
    
main()