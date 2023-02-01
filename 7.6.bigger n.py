# function to print numbers from list that bigger than certain number

# global constants
CONTROL_NUMBER = 5


def main():
    # make a list of numbers
    numbers = [2, 5, 9, 45, 200, 235, 634]
    find_bigger_numbers(numbers, CONTROL_NUMBER)


def find_bigger_numbers(check_list, control_number):
    # make a list of numbers from argument list that bigger, than argument number
    bigger_numbers = [number for number in check_list if number > control_number]
    # print bigger numbers from list
    for number in bigger_numbers:
        print(number)

# Call the main function.
if __name__ == '__main__':
    main()
