# program to analyze results of power ball lottery from data in file

# global constants
FILE_NAME = 'pbnumbers.txt'
MOST_FREQUENT = 10
LEAST_FREQUENT = 10
READY_NUMBERS = 10


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        data_list = infile.readlines()
        infile.close()
        get_most_least(data_list)
        print()
        get_ready(data_list)
        print()
        get_all_freq(data_list)

    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


def get_most_least(in_list):
    all_numbers_list = []
    for line in in_list:
        line = line.rstrip('\n')
        line_number_list = [int(n) for n in line.split()]
        all_numbers_list += line_number_list
    numbers_quantity = [0] * 69
    # write frequencies of numbers
    for number in all_numbers_list:
        numbers_quantity[number - 1] += 1
    # get and print ten most frequent numbers
    numbers_quantity2 = [] + numbers_quantity
    most_frequent_numbers = [0] * MOST_FREQUENT
    most_frequent_numbers_freq = [0] * MOST_FREQUENT
    for i in range(MOST_FREQUENT):
        most_frequent_numbers[i] = numbers_quantity2.index(max(numbers_quantity2)) + 1
        most_frequent_numbers_freq[i] = max(numbers_quantity2)
        # remove most frequent number to get a next one
        numbers_quantity2[numbers_quantity2.index(max(numbers_quantity2))] = -1
    print('Most frequent numbers')
    print('Number\tFrequency')
    for i in range(MOST_FREQUENT):
        print(f'{most_frequent_numbers[i]:^6}\t{most_frequent_numbers_freq[i]:^9}')
    # get and print ten least frequent numbers
    numbers_quantity3 = [] + numbers_quantity
    least_frequent_numbers = [0] * LEAST_FREQUENT
    least_frequent_numbers_freq = [0] * LEAST_FREQUENT
    for i in range(LEAST_FREQUENT):
        least_frequent_numbers[i] = numbers_quantity3.index(min(numbers_quantity3)) + 1
        least_frequent_numbers_freq[i] = min(numbers_quantity3)
        # remove least frequent number to get a next one
        numbers_quantity3[numbers_quantity3.index(min(numbers_quantity3))] = max(numbers_quantity3)
    print()
    print('Least frequent numbers')
    print('Number\tFrequency')
    for i in range(LEAST_FREQUENT):
        print(f'{least_frequent_numbers[i]:^6}\t{least_frequent_numbers_freq[i]:^9}')


def get_ready(in_list):
    # make list to count when every 69 number was used last time, 0 - never been used, 654 - latest time used
    count_list = [0] * 69
    # make iterations counter
    it_counter = 1
    # make a map for how long ago every number was used
    for line in in_list:
        line = line.rstrip('\n')
        line_number_list = [int(n) for n in line.split()]
        for n in line_number_list:
            count_list[n - 1] = it_counter
        it_counter += 1
    # get and print ten least frequent numbers
    ready_numbers = [0] * READY_NUMBERS
    for i in range(READY_NUMBERS):
        ready_numbers[i] = count_list.index(min(count_list)) + 1
        # remove min number to get a next one
        count_list[count_list.index(min(count_list))] = max(count_list)
    print('Most ready numbers (the earlier the more ready)')
    for i in range(READY_NUMBERS):
        print(f'{ready_numbers[i]:^9}')


def get_all_freq(in_list):
    number69_list = []
    pwnumbers_list = []
    for line in in_list:
        line = line.rstrip('\n')
        line_number_list = [int(n) for n in line.split()]
        # divide power ball numbers from others (every 6th number in line)
        index = 0
        for n in line_number_list:
            if index < 5:
                number69_list.append(n)
                index += 1
            elif index == 5:
                pwnumbers_list.append(n)
    # count and print frequencies of numbers 1-69
    # make mask
    numbers69_frequency = [0] * 69
    # write frequencies of numbers
    for n in number69_list:
        numbers69_frequency[n - 1] += 1
    # print data
    print('Frequency of numbers 1-69')
    print('Number\tFrequency')
    index1 = 0
    for freq in numbers69_frequency:
        print(f'{index1 + 1:^6}\t{freq:^9}')
        index1 += 1
    # count and print frequencies of power ball numbers 1-26
    # make mask
    pwnumbers26_frequency = [0] * 26
    # write frequencies of numbers
    for n in pwnumbers_list:
        pwnumbers26_frequency[n - 1] += 1
    # print data
    print()
    print('Frequency of power ball numbers')
    print('Number\tFrequency')
    index2 = 0
    for freq in pwnumbers26_frequency:
        print(f'{index2 + 1:^6}\t{freq:^9}')
        index2 += 1


# Call the main function.
if __name__ == '__main__':
    main()
