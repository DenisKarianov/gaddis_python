# program to analyze characters from data in file

# global constants
FILE_NAME = 'text.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        content_file = infile.read()
        infile.close()
        # declare variables to count characters
        upper_letters = 0
        lower_letters = 0
        digits = 0
        spaces = 0
        undefined_char = 0
        for ch in content_file:
            if ch.isalpha():
                if ch.isupper():
                    upper_letters += 1
                else:
                    lower_letters += 1
            elif ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
            else:
                undefined_char += 1
        print(f'Uppercase letters: {upper_letters}')
        print(f'Lowercase letters: {lower_letters}')
        print(f'Digits: {digits}')
        print(f'Space characters: {spaces}')
        print(f'Undefined characters: {undefined_char}')
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')

    # Call the main function.


if __name__ == '__main__':
    main()
