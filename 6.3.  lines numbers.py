# program read 1st five lines from file, print it.


def main():
    file_to_open = input('Enter a name of the file: ')
    input_file = open(file_to_open, 'r')  # open a file for reading
    counter = 1  # declare line counter
    for line in input_file:
        line = line.rstrip('\n')
        print(f'{counter}: {line}')
        counter += 1


main()
