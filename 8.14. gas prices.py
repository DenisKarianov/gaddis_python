# program to analyze gas prices from data in file

# global constants
FILE_NAME = 'GasPrices.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        data_list = infile.readlines()
        infile.close()
        year_average_price(data_list)


    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


def year_average_price(in_list):
    dates = []
    prices = []
    for line in in_list:
        line = line.rstrip('\n')
        # divide dates from prices to different lists
        index = 0
        for data in line.split(':'):
            if index == 0:
                dates.append([int(d) for d in data.split('-')])  # make 2d-list
                index += 1
            else:
                prices.append(float(data))
    # count year_average_price
    loop_counter = 0
    year_counter = 0
    current_year = dates[0][2]
    one_year_total = 0.0
    year_average_prices = []
    for date in dates:
        if date[2] == current_year:
            if loop_counter < len(dates) - 1:
                one_year_total += prices[loop_counter]
                loop_counter += 1
                year_counter += 1
            else:
                one_year_total += prices[loop_counter]
                year_counter += 1
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for last year
        else:
            if loop_counter < len(dates) - 1:
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for one year
                current_year = date[2]
                one_year_total = 0.0
                one_year_total += prices[loop_counter]
                loop_counter += 1
                year_counter = 1
            else:
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for one year
                year_average_prices.append([date[2], prices[loop_counter]])  # save data for last year
    # print data
    print('Year_average_prices')
    print('Year\tPrice')
    for data in year_average_prices:
        print(f'{data[0]:^4}\t{data[1]:^7.4f}')


# Call the main function.
if __name__ == '__main__':
    main()
