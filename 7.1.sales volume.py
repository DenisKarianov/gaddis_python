# program to calculate sales volume for a week

def main():
    # make a blank list.
    sales_list = [0] * 7
    # input sales data in list
    for index in range(7):
         sales_list[index] = float(input(f'Enter sales for day #{index + 1}: '))

    # declare a variable to count sales volume
    total = 0.0
    # loop to count sales volume
    for number in sales_list:
        total += number
    print(f'Sales volume for this week: {total}')


# Call the main function.
if __name__ == '__main__':
    main()
