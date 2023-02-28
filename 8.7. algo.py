# function that accept string and print it in reverse order

# global constants
TEST_STRING = 'aegeg89'
def main():
    reverse_string(TEST_STRING)


def reverse_string(str):
    # declare variable for last character in string
    index = -1
    while index >= - (len(str)):
        print(str[index], end='')
        index -= 1


# Call the main function.
if __name__ == '__main__':
    main()
