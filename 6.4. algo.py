# program read numbers from file, print it and close file.


def main():
    input_file = open('number_list.txt', 'r') # open a file for reading
    for line in input_file:
        print(line.rstrip('\n'))
    input_file.close()


main()
