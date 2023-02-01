# make 2d list and get data for elements in it form user

# Constants for rows and columns
ROWS = 5
COLS = 3

def main():
    # Create a two-dimensional list.
    number_list = [0] * ROWS
    index = 0
    while index < len(number_list):
        number_list[index] = [0] * COLS
        index += 1
    # user inserts data in 2d list
    for r in range(ROWS):
        for c in range(COLS):
            number_list[r][c] = int(input('Enter integer: '))
    print(number_list)


# Call the main function.
if __name__ == '__main__':
    main()
