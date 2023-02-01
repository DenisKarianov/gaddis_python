# program shows all lines in file data.txt


def main():
    data_file = open('data.txt', 'r') # open a file for reading
    line = data_file.readline()
    while line != '':
        print(line)
        line = data_file.readline()
    data_file.close()


main()
