# program read 1st five lines from file, print it.


def main():
    file_to_open = input('Enter a name of the file: ')
    input_file = open(file_to_open, 'r')  # open a file for reading
    counter = 1  # declare loop counter
    line = input_file.readline()  # read 1st line
    while line != '' and counter <= 5:
        print(line, end='')
        counter += 1
        line = input_file.readline()  # read next line


main()
