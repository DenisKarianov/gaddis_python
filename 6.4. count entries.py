# program count entries from file and print it.

# global constants
FILE_NAME = 'number_list.txt'

def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    counter = 0  # declare line counter
    for line in input_file:
        counter += 1
    print(counter)


main()
