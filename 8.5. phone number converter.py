# program to convert phone number with letters to only numbers

# make tuple for symbols
letters_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
numbers_tuple = (2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9)


def main():
    # get phone number from user
    user_data = input('Please, enter a phone number to convert to number without letters: ')
    # check if there is digit in phone number
    if not user_data.isdigit():
        print(get_numbers_phone(user_data))
    else:
        print('Entered phone number contains only digits.')
        print(user_data)


def get_numbers_phone(phone):
    # check if string is uppercase
    user_data_uppercase = ""
    if phone.isupper():
        user_data_uppercase = phone
    else:
        # make string uppercase
        for i in phone:
            user_data_uppercase += i.upper()
    # make empty string for converted phone number
    conv_phone_number = ""
    for ele in user_data_uppercase:
        if ele.isalpha():
            try:
                symbol_index = letters_tuple.index(ele)
                conv_phone_number += str(numbers_tuple[symbol_index])
            except ValueError:
                print(f'Symbol {ele} is not accepted.')
        else:
            conv_phone_number += ele
    return conv_phone_number


# Call the main function.
if __name__ == '__main__':
    main()
