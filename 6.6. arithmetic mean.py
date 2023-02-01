# program count sum of numbers in file and print it.

# global constants
FILE_NAME = 'numbers.txt'


def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    amount = 0  # declare a variable to count sum of numbers
    counter = 0  # declare a variable to count quantity of numbers
    for line in input_file:
        amount += int(line)
        counter += 1
    input_file.close()
    print(amount / counter)


main()
