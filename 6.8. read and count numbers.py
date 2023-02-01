# program count sum and quantity of numbers in file and print it and numbers.

# global constants
FILE_NAME = 'random_numbers_list.txt'


def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    amount = 0  # declare a variable to count sum of numbers
    counter = 0  # declare a variable to count quantity of numbers
    for line in input_file:
        number = int(line)
        print(number)
        amount += number
        counter += 1
    input_file.close()
    print(f'Amount of numbers is {amount}.')
    print(f'Quantity of numbers is {counter}.')


main()
