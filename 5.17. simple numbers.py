# define simple number


def is_prime(number):
    if number % 1 == 0 and number > 2:  # define if number is whole and > 2
        composite_number_flag = 0  # declare a variable for composite number flag
        counter = number - 1  # declare decreasing divisor, that check number for composite
        while composite_number_flag == 0 and counter > 1:
            if number % counter == 0:
                composite_number_flag += 1
            else:
                counter -= 1
        if composite_number_flag == 0:
            status = True
        else:
            status = False
    elif number == 2:
        status = True
    else:
        status = False
    return status


def main():
    # get natural number from user
    number = int(input('Enter natural number: '))

    # check if number is simple
    if is_prime(number):
        print(f'Number {number} is simple.')
    else:
        print(f'Number {number} is not simple.')


main()
