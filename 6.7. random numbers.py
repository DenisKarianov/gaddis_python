# program count sum of numbers in file and print it.

import random

# global constants
FILE_NAME = 'random_numbers_list.txt'
MIN = 1
MAX = 500

def main():
    numbers_quantity = int(input('Enter a quantity of numbers: '))
    output_file = open(FILE_NAME, 'w')  # open a file for writing
    for i in range(numbers_quantity):
        number = random.randint(MIN, MAX)
        output_file.write(f'{number}\n')
    output_file.close()
    print(f'{numbers_quantity} numbers were written to file.')


main()
