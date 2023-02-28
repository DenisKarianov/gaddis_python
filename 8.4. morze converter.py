# program to convert string to morze code from user's data

# make tuple for symbols
symbols_tuple = (' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
                 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
morze_tuple = (' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-',
               '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.',
               '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
               '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..')


def main():
    # get string from user
    user_data = input('Please, enter a word to convert to Morze code: ')
    # check if string is uppercase
    if user_data.isupper():
        print(get_morze(user_data))
    else:
        # make string uppercase
        user_data_uppercase = ""
        for i in user_data:
            user_data_uppercase += i.upper()
        print(get_morze(user_data_uppercase))



def get_morze(string):
    # make empty string for morze symbols
    str1 = ""
    for ch in string:
        try:
            symbol_index = symbols_tuple.index(ch)
            str1 += morze_tuple[symbol_index]
            str1 += ' '
        except ValueError:
            print(f'Symbol {ch} is not accepted.')
    return str1


# Call the main function.
if __name__ == '__main__':
    main()
