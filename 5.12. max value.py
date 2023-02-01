# show bigger value from two
def main():
    # ask user for two whole numbers
    first_number = int(input('Enter first whole number: '))
    second_number = int(input('Enter second whole number: '))

    # call function to get bigger number
    bigger_number = get_bigger_number(first_number, second_number)

    # print bigger number
    print(f'Bigger number is {bigger_number}')


def get_bigger_number(first_number, second_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number


main()
