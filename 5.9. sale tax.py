# count sale taxes

# global constants
FED_TAX_RATE = 0.05
MUN_TAX_RATE = 0.025


def main():
    # ask user for data
    month_sale = float(input('Please input month sales volume: '))
    # call for count and print function
    show_taxes(month_sale)


def show_taxes(sale):
    mun_tax = sale * MUN_TAX_RATE
    fed_tax = sale * FED_TAX_RATE
    print(f'Municipal sale tax: {sale * MUN_TAX_RATE}.')
    print(f'Federal sale tax: {sale * FED_TAX_RATE}.')
    print(f'Total sale tax: {sale * MUN_TAX_RATE + sale * FED_TAX_RATE}.')


main()
