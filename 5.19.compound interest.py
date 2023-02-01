# count compound interest

# function to count compound interest
def get_compound_interest(current_amount, monthly_interest_rate, month_quantity):
    future_amount = current_amount * (1 + monthly_interest_rate/100) ** month_quantity
    return future_amount


def main():
    # get values from user
    current_amount = float(input('Enter current amount: '))
    monthly_interest_rate = float(input('Enter monthly interest rate: '))
    month_quantity = int(input('Enter month quantity: '))

    # call for get_compound_interest function and print result
    future_amount = get_compound_interest(current_amount, monthly_interest_rate, month_quantity)
    print(f'After {month_quantity} months your amount {current_amount} become {future_amount:.2f}.')


main()
