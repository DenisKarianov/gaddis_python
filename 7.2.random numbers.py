# program to generate 7 random numbers, assign them to list and print them
import random

def main():
    # make a blank list.
    numbers_list = [0] * 7
    # assign random numbers 0-9 to elements in list
    for index in range(7):
         numbers_list[index] = random.randint(0, 9)
    for number in numbers_list:
        print(number)


# Call the main function.
if __name__ == '__main__':
    main()
