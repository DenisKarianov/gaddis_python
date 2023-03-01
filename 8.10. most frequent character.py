# program to define most frequent character in string

def main():
    # get data from user
    user_data = input('Please, enter a string: ')
    most_qty = 0
    most_common_item = ''
    for ch in user_data:
        qty = user_data.count(ch)
        if qty > most_qty:
            most_qty = qty
            most_common_item = ch
    print(f'Most common character "{most_common_item}" occurs {most_qty} times.')


# Call the main function.
if __name__ == '__main__':
    main()
