# generate random numbers and count quantity of even and non-even numbers
import random

# global constants
MIN_NUMBER = 1
MAX_NUMBER = 1000
NUMBER_QUANTITY = 100


def is_even(number):
    if number % 2 == 0:
        status = True
    else:
        status = False
    return status


def main():
    # declare variables
    total_even_numbers = 0
    total_non_even_numbers = 0

    # generate numbers and count even and non-even
    for i in range(NUMBER_QUANTITY):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if is_even(number):
            total_even_numbers += 1
        else:
            total_non_even_numbers += 1

    # print even and non-even numbers quantity
    print(f'Total even numbers quantity: {total_even_numbers}.')
    print(f'Total non-even numbers quantity: {total_non_even_numbers}.')


main()
