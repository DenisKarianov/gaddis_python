# program read name from file my_name.txt, print it and close file.


def main():
    input_file = open('my_name.txt', 'r') # open a file for reading
    data = input_file.read()
    input_file.close()
    print(data)


main()
