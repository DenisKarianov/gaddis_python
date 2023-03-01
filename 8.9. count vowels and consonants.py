# program to count vowels and consonants in string

# make tuples for symbols
vowels_tuple = ('A', 'E', 'I', 'O', 'U', 'Y')


def main():
    # get data from user
    user_data = input('Please, enter a string: ')
    print(f'Vowels: {count_vowels(user_data)}.')
    print(f'Consonants: {count_consonants(user_data)}.')


def count_vowels(in_string):
    # variable to count vowels
    total = 0
    for ch in in_string:
        if ch.isalpha():
            if ch.upper() in vowels_tuple:
                total += 1
    return total


def count_consonants(in_string):
    # variable to count consonants
    total = 0
    for ch in in_string:
        if ch.isalpha():
            if ch.upper() not in vowels_tuple:
                total += 1
    return total


# Call the main function.
if __name__ == '__main__':
    main()
