# program read numbers from file, print it and close file.


def main():
    input_file = open('numbers.txt', 'r') # open a file for reading
    for line in input_file:
        print(int(line))
    input_file.close()


main()
