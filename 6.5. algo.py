# program read numbers from file, count sum of numbers, print it and close file.


def main():
    input_file = open('number_list.txt', 'r') # open a file for reading
    total = 0
    for line in input_file:
        amount = float(line)
        total += amount
    input_file.close()
    print(f'{total}')


main()
