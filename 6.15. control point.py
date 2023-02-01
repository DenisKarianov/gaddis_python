# program shows all lines in file data.txt


def main():
    data_file = open('data.txt', 'r') # open a file for reading
    for line in data_file:
        print(line)
    data_file.close()


main()
