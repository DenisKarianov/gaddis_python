# program opens file, use a loop to write to a file numbers 1-100 and close file.


def main():
    output_file = open('number_list.txt', 'w') # open a file for writing
    for number in range(1,101):
        output_file.write(f'{number}\n')

    output_file.close()


main()
