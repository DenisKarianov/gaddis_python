# program to print date from data in string

def main():
    # get date from user in format dd/mm/year
    user_data = input('Please, enter a date in format dd/mm/year: ')
    # make list of month
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    user_data_list = user_data.split('/')
    if int(user_data_list[0]) == 1:
        print(f'1st of {month_list[int(user_data_list[1]) - 1]}, {user_data_list[2]}')
    elif int(user_data_list[0]) == 2:
        print(f'2nd of {month_list[int(user_data_list[1]) - 1]}, {user_data_list[2]}')
    else:
        print(f"{user_data_list[0]}th of {month_list[int(user_data_list[1]) - 1]}, {user_data_list[2]}")


# Call the main function.
if __name__ == '__main__':
    main()
