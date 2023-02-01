# make simple number list

# declare global constants
MIN_NUMBER = 1
MAX_NUMBER = 100


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
    print(f'Simple numbers in range from {MIN_NUMBER} to {MAX_NUMBER}:')
    for number in range(MIN_NUMBER, MAX_NUMBER + 1):
        if is_prime(number):
            print(f'{number}', end=' ')


main()
