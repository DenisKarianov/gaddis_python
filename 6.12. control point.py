# loop 'for' for write numbers 1-10 to file


def main():
    numbers_file = open('numbers.txt', 'w') # open a file for writing
    for count in range(1, 11):
        numbers_file.write(f'{count}\n')
    numbers_file.close()


main()
