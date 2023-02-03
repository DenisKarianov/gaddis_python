# program to calculate population data

# global constants
FILE_NAME = 'USPopulation.txt'
FIRST_YEAR = 1950


def main():
    try:
        # read population data from file to list
        infile = open(FILE_NAME, 'r')
        population_list = infile.readlines()
        infile.close()
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')
    # transform str to int in list
    population_list = int_list(population_list)
    # count average year change
    average_year_change = (population_list[-1] - population_list[0]) / len(population_list)
    # make list of population changes for every year
    population_change_list = []
    index = 0
    while index < len(population_list) - 1:
        population_change_list.append(population_list[index + 1] - population_list[index])
        index += 1
    # get year with max change
    max_change_year = FIRST_YEAR + 1 + population_change_list.index(max(population_change_list))
    # get year with min change
    min_change_year = FIRST_YEAR + 1 + population_change_list.index(min(population_change_list))
    print(f'Average year change: {average_year_change:.0f}.')
    print(f'Year with max population change: {max_change_year}.')
    print(f'Year with min population change: {min_change_year}.')

def int_list(list):
    index = 0
    while index < len(list):
        list[index] = int(list[index])
        index += 1
    return list



# Call the main function.
if __name__ == '__main__':
    main()
