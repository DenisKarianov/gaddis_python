# программа по конверитрованию километров в мили
def main():
    number = float (input ('Введите расстояние в км: '))
    miles_value = km_to_miles(number)
    print (f'{number} километров составляет {miles_value:.2f} миль.')

def km_to_miles(km):
    return km * 0.6214

main()