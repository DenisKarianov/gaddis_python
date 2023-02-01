# This program assigns random numbers to
# a two-dimensional list and print them by using nested loop.

# Constants for rows and columns
ROWS = 3
COLS = 4

def main():
    # Create a two-dimensional list.
    values = [0] * ROWS
    index = 0
    while index < len(values):
        values[index] = [0] * COLS
        index += 1
    print(values)

# Call the main function.
if __name__ == '__main__':
    main()