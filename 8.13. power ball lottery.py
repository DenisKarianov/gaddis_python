# program to analyze results of power ball lottery from data in file

# global constants
FILE_NAME = 'pbnumbers.txt'
MOST_FREQUENT = 10
LEAST_FREQUENT = 10
# numbers_quantity = [0] * 69

pw_numbers_quantity = [0] * 26


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        data_list = infile.readlines()
        infile.close()
        get_most_common(data_list)

    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


def get_most_common(in_list):
    all_numbers_list = []
    for line in in_list:
        line = line.rstrip('\n')
        line_list = line.split()
        line_number_list = [int(n) for n in line_list]
        all_numbers_list += line_number_list
    numbers_quantity = [0] * 69
    # write frequencies of numbers
    for number in all_numbers_list:
        numbers_quantity[number - 1] += 1
    # get and print ten most frequent numbers
    numbers_quantity2 = [] + numbers_quantity
    most_frequant_numbers = [0] * MOST_FREQUENT
    most_frequant_numbers_freq = [0] * MOST_FREQUENT
    for i in range(MOST_FREQUENT):
        most_frequant_numbers[i] = numbers_quantity2.index(max(numbers_quantity2)) + 1
        most_frequant_numbers_freq[i] = max(numbers_quantity2)
        # remove most frequent number to get a next one
        numbers_quantity2[numbers_quantity2.index(max(numbers_quantity2))] = -1
    print('Most frequent numbers')
    print('Number\tFrequency')
    for i in range(MOST_FREQUENT):
        print(f'{most_frequant_numbers[i]:^6}\t{most_frequant_numbers_freq[i]:^9}')
    # get and print ten least frequent numbers
    numbers_quantity3 = [] + numbers_quantity
    least_frequant_numbers = [0] * LEAST_FREQUENT
    least_frequant_numbers_freq = [0] * LEAST_FREQUENT
    for i in range(LEAST_FREQUENT):
        least_frequant_numbers[i] = numbers_quantity3.index(min(numbers_quantity3)) + 1
        least_frequant_numbers_freq[i] = min(numbers_quantity3)
        # remove least frequent number to get a next one
        numbers_quantity3[numbers_quantity3.index(min(numbers_quantity3))] = max(numbers_quantity3)
    print()
    print('Least frequent numbers')
    print('Number\tFrequency')
    for i in range(LEAST_FREQUENT):
        print(f'{least_frequant_numbers[i]:^6}\t{least_frequant_numbers_freq[i]:^9}')


# Call the main function.
if __name__ == '__main__':
    main()
