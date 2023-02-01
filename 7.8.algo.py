# list2 from list1

def main():
    # make a list of numbers
    numbers = [2, 5, 9, 45, 200, 235, 634]
    # make a list of squared numbers from 1st list
    squared_numbers = [number ** 2 for number in numbers]
    # make list of numbers > 100
    big_numbers = [number for number in numbers if number > 100]
    # make list of even numbers
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(squared_numbers)
    print(big_numbers)
    print(even_numbers)


# Call the main function.
if __name__ == '__main__':
    main()
