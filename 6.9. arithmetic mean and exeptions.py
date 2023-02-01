# program count sum of numbers in file and print it.

# global constants
FILE_NAME = 'numbers.txt'


def main():
    try:
        input_file = open(FILE_NAME, 'r')  # open a file for reading
        amount = 0  # declare a variable to count sum of numbers
        counter = 0  # declare a variable to count quantity of numbers
        for line in input_file:
            amount += int(line)
            counter += 1
        print(amount / counter)
    except IOError:
        print(f"Error with {FILE_NAME} file.")
    except ValueError:
        print(f'Values in {FILE_NAME} file are not integer.')
    input_file.close()


main()
