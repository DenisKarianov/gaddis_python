# program to count sum of numbers in string

def main():
    # get numbers from user
    user_numbers_string = input('Please, enter one-digit numbers without spaces: ')
    # declare a variable to count sum of numbers
    total = 0
    for number in user_numbers_string:
        total += int(number)
    print(f'Sum of all entered numbers is {total}.')


# Call the main function.
if __name__ == '__main__':
    main()
