# program to save in list data for rainfall

def main():
    # make a blank list.
    rainfall = [0] * 12
    # user insert rainfall data in list
    for index in range(12):
         rainfall[index] = float(input(f'Enter rainfall data for month #{index + 1}: '))
    # declare a accumulative variable to count rainfall for whole year
    year_rainfall = 0.0
    # count year rainfall
    for month in rainfall:
        year_rainfall += month
    # print results
    print(f'Year rainfall: {year_rainfall}')
    print(f'Average month rainfall: {year_rainfall / len(rainfall):.0f}')
    print(f'Maximum month rainfall: {max(rainfall)}')
    print(f'Minimum month rainfall: {min(rainfall)}')




# Call the main function.
if __name__ == '__main__':
    main()
