# user should guess random number

import random

# global constants
MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    print('You should guess a number!')
    is_guessed()
    print('Game is over.')


def is_guessed():
    continue_flag = 'y'  # declare a variable for conditional loop
    loop_count = 0 # declare a variable to count attempts
    while continue_flag == 'y' or continue_flag == 'Y' or continue_flag == 'yes' or continue_flag == 'YES':
        # generate random number if it is start of the game
        if loop_count == 0:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)

        # get values from user
        user_input = input(f'Guess whole number from {MIN_NUMBER} to {MAX_NUMBER} or enter "n" to quit the game: ')
        if user_input.isdigit(): # check if user wants to guess or quit game
            user_number_int = int(user_input)
            loop_count += 1  # count quantity of attempts
            if user_number_int == number:
                print(f'Congratulation, you have guessed the number! It was your attempt #{loop_count}.')
                loop_count = 0  # null quantity of attempts
            elif user_number_int > number:
                print('Too big number, try again!')
            else:
                print('Too little number, try again!')
        else:
            continue_flag = user_input


main()
