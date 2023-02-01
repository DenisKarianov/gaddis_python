# program count sum of numbers in file and print it.

# global constants
FILE_NAME = 'numbers.txt'

def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    amount = 0
    for line in input_file:
        amount += int(line)
    input_file.close()
    print(amount)


main()
