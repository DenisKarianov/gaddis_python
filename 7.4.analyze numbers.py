# program to save in list numbers and make some calculations with them

# global constants
NUMBERS_QUANTITY = 20


def main():
    # make a blank list.
    numbers = [0] * NUMBERS_QUANTITY
    # user insert numbers in list
    for index in range(NUMBERS_QUANTITY):
        numbers[index] = float(input(f'Enter number #{index + 1} from {NUMBERS_QUANTITY}: '))
    # declare a accumulative variable to count sum of numbers
    total = 0.0
    # count sum of numbers
    for number in numbers:
        total += number
    # print results
    print(f'Minimum number: {min(numbers)}')
    print(f'Maximum number: {max(numbers)}')
    print(f'Sum of numbers: {total}')
    print(f'Average number: {total / len(numbers):.2f}')


# Call the main function.
if __name__ == '__main__':
    main()
