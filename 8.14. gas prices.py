# program to analyze gas prices from data in file

# global constants
FILE_NAME = 'GasPrices.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        data_list = infile.readlines()
        infile.close()
        year_average_max_min_price(data_list)
        month_average_price(data_list)
        sort_prices(data_list)
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


def year_average_max_min_price(in_list):
    dates, prices = get_dates_prices(in_list)
    # count year_average_price
    loop_counter = 0
    year_counter = 0
    current_year = dates[0][2]
    one_year_total = 0.0
    year_average_prices = []
    one_year_prices = []  # list to save prices for current year to get max and min prices for the year
    one_year_dates = []  # list to save dates for current year to get dates of max and min prices for the year
    max_min_year_price = []  # list to save max and min prices and dates in every year
    for date in dates:
        if date[2] == current_year:
            if loop_counter < len(dates) - 1:
                one_year_total += prices[loop_counter]
                one_year_prices.append(prices[loop_counter])  # add price to make list of prices for current year
                one_year_dates.append(dates[loop_counter])  # add date to make list of dates for current year
                loop_counter += 1
                year_counter += 1
            else:
                one_year_total += prices[loop_counter]
                one_year_prices.append(prices[loop_counter])  # add price to make list of prices for current year
                one_year_dates.append(dates[loop_counter])  # add date to make list of dates for current year
                year_counter += 1
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for last year
                # save date about year, max, min prices and dates of max and min prices for current year to list
                max_date = get_string_date(one_year_dates[one_year_prices.index(max(one_year_prices))], '-')
                min_date = get_string_date(one_year_dates[one_year_prices.index(min(one_year_prices))], '-')
                max_min_year_price.append(
                    [current_year, max(one_year_prices), max_date, min(one_year_prices), min_date])
        else:
            if loop_counter < len(dates) - 1:
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for one year
                # save date about year, max, min prices and dates of max and min prices for current year to list
                max_date = get_string_date(one_year_dates[one_year_prices.index(max(one_year_prices))], '-')
                min_date = get_string_date(one_year_dates[one_year_prices.index(min(one_year_prices))], '-')
                max_min_year_price.append(
                    [current_year, max(one_year_prices), max_date, min(one_year_prices), min_date])
                one_year_prices = []  # erase data for new year
                one_year_dates = []  # erase data for new year
                current_year = date[2]
                one_year_total = 0.0  # erase total sum of prices for counting average price for year
                one_year_total += prices[loop_counter]
                one_year_prices.append(prices[loop_counter])  # add price to make list of prices for current year
                one_year_dates.append(dates[loop_counter])  # # add dates to make list of dates for current year
                loop_counter += 1
                year_counter = 1
            else:  # if in the end of data there's one line with data about new year
                year_average_prices.append([current_year, one_year_total / year_counter])  # save data for one year
                year_average_prices.append([date[2], prices[loop_counter]])  # save data for last year
                # save date about year, max, min prices and dates of max and min prices for current year to list
                max_date = get_string_date(one_year_dates[one_year_prices.index(max(one_year_prices))], '-')
                min_date = get_string_date(one_year_dates[one_year_prices.index(min(one_year_prices))], '-')
                max_min_year_price.append(
                    [current_year, max(one_year_prices), max_date, min(one_year_prices), min_date])
                # save date about year, max and min price for last year to list
                max_min_year_price.append(
                    [date[2], prices[loop_counter], dates[loop_counter], prices[loop_counter], dates[loop_counter]])
    # print data
    print("Year prices' data")
    print("Year\tAverage price\tMax price\tMax price's date\tMin price\tMin price's date")
    index = 0
    while index < len(year_average_prices):
        print(
            f'{year_average_prices[index][0]:^4}\t{year_average_prices[index][1]:^14.4f}'
            f'\t{max_min_year_price[index][1]:^9}\t{max_min_year_price[index][2]:^16}'
            f'\t{max_min_year_price[index][3]:^9}\t{max_min_year_price[index][4]:^16}')
        index += 1


def month_average_price(in_list):
    dates, prices = get_dates_prices(in_list)
    # count month_average_price
    loop_counter = 0
    month_counter = 0
    current_year = dates[0][2]
    current_month = dates[0][0]
    current_month_total = 0.0
    years_numbers = []
    month_average_prices = []
    all_av_prices = []
    for date in dates:
        if date[2] == current_year:  # year the same
            if loop_counter < len(dates) - 1:  # not the last line
                if date[0] == current_month:  # month the same
                    current_month_total += prices[loop_counter]
                    loop_counter += 1
                    month_counter += 1
                else:  # month changed
                    month_average_prices.append(
                        [current_month, current_month_total / month_counter])  # save data for one month
                    current_month = date[0]  # new current month
                    current_month_total = 0.0  # erase total sum of prices for counting average price for month
                    current_month_total += prices[loop_counter]
                    loop_counter += 1
                    month_counter = 1
            else:  # if last line
                years_numbers.append(current_year)  # save year number
                if date[0] == current_month:  # month the same
                    current_month_total += prices[loop_counter]
                    month_counter += 1
                    # save data for last month
                    month_average_prices.append([current_month, current_month_total / month_counter])
                    # save data for year in final list
                    all_av_prices.append(month_average_prices)
                else:  # month changed
                    # save data for month before last
                    month_average_prices.append([current_month, current_month_total / month_counter])
                    # save data for last month
                    month_average_prices.append([date[0], prices[loop_counter]])
                    # save data for year in final list
                    all_av_prices.append(month_average_prices)
        else:  # year changed
            if loop_counter < len(dates) - 1:  # not the last line
                years_numbers.append(current_year)  # save year number
                current_year = date[2]  # new current year
                # month changed too
                month_average_prices.append(
                    [current_month, current_month_total / month_counter])  # save data for month before
                # save data for year in final list
                all_av_prices.append(month_average_prices)
                month_average_prices = []  # erase list for new year
                current_month = date[0]  # new current month
                current_month_total = 0.0  # erase total sum of prices for counting average price for month
                current_month_total += prices[loop_counter]
                loop_counter += 1
                month_counter = 1
            else:  # last line
                years_numbers.append(current_year)  # save number of year before
                years_numbers.append(date[2])  # save number of last year
                # month changed too
                month_average_prices.append(
                    [current_month, current_month_total / month_counter])  # save data for month before
                # save data for year in final list
                all_av_prices.append(month_average_prices)
                month_average_prices = []  # erase list for new year
                month_average_prices.append([date[0], prices[loop_counter]])  # save data for last month
                # save data for last year in final list
                all_av_prices.append(month_average_prices)
    # print data
    print()
    print("Month average prices")
    year = 'Year'
    jan = 'Jan'
    feb = 'Feb'
    mar = 'Mar'
    apr = 'Apr'
    may = 'May'
    jun = 'Jun'
    jul = 'Jul'
    aug = 'Aug'
    sep = 'Sep'
    oct = 'Oct'
    nov = 'Nov'
    dec = 'Dec'
    print(
        f"{year:^4}\t{jan:^5}\t{feb:^5}\t{mar:^5}\t{apr:^5}\t{may:^5}\t{jun:^5}\t{jul:^5}\t{aug:^5}\t{sep:^5}\t"
        f"{oct:^5}\t{nov:^5}\t{dec:^5}")
    index = 0
    while index < len(all_av_prices):
        one_year_2dlist = all_av_prices[index]
        month_print_list = [0] * 12
        # write average prices to places in list, that depends on month
        index2 = 0
        while index2 < len(range(12)):
            if index2 < len(one_year_2dlist):
                month_print_list[int(one_year_2dlist[index2][0]) - 1] = round(float(one_year_2dlist[index2][1]), 4)
                index2 += 1
            else:
                index2 += 1
        # change 0 to '---' so if no data for certain month it still prints in appropriate order
        index3 = 0
        while index3 < len(month_print_list):
            if month_print_list[index3] == 0:
                month_print_list[index3] = '---'
                index3 += 1
            else:
                index3 += 1
        print(
            f"{years_numbers[index]:^4}\t{month_print_list[0]:^5}\t{month_print_list[1]:^5}\t{month_print_list[2]:^5}\t"
            f"{month_print_list[3]:^5}\t{month_print_list[4]:^5}\t{month_print_list[5]:^5}\t{month_print_list[6]:^5}\t"
            f"{month_print_list[7]:^5}\t{month_print_list[8]:^5}\t{month_print_list[9]:^5}\t{month_print_list[10]:^5}\t"
            f"{month_print_list[11]:^5}")
        index += 1


# function to make string date from date in list format, divider - symbol between numbers in date,
# should be string
def get_string_date(date_list, divider):
    date_str = ''
    counter = 0  # to count iterations to don't add divider in the end of date
    for d in date_list:
        date_str += str(d)
        counter += 1
        if counter < len(date_list):
            date_str += divider
    return date_str


# function to transform data from file into 2 lists - prices and dates
def get_dates_prices(in_list):
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
    return dates, prices


def sort_prices(in_list):
    dates, prices = get_dates_prices(in_list)
    # sort from min to max
    prices2 = [] + prices
    min_sort = []
    max_value = max(prices2)
    index = 0
    while index < len(prices2):
        min_value = min(prices2)
        if min_value <= max_value:
            # copy date and min_value to sorted list
            min_sort.append([get_string_date(dates[prices2.index(min(prices2))], '-'), min_value])
            # remove min value to get next one
            prices2[prices2.index(min(prices2))] = max(prices2) + 1
        index += 1
    # save sorted data in txt file
    min_sort_file = open('min_sort.txt', 'w')
    for i in min_sort:
        min_sort_file.write(f'{i[0]}:{i[1]}\n')
    min_sort_file.close()
    print()
    print(f'List, sorted from min to max, saved to min_sort.txt.')
    # sort from max to min
    prices3 = [] + prices
    max_sort = []
    min_value = min(prices3)
    index = 0
    while index < len(prices3):
        max_value = max(prices3)
        if max_value >= min_value:
            # copy date and min_value to sorted list
            max_sort.append([get_string_date(dates[prices3.index(max(prices3))], '-'), max_value])
            # remove max value to get next one
            prices3[prices3.index(max(prices3))] = min(prices3) - 1
        index += 1
    # save sorted data in txt file
    max_sort_file = open('max_sort.txt', 'w')
    for i in max_sort:
        max_sort_file.write(f'{i[0]}:{i[1]}\n')
    max_sort_file.close()
    print(f'List, sorted from max to min, saved to max_sort.txt.')





# Call the main function.
if __name__ == '__main__':
    main()
