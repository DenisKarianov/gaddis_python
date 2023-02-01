# game with user "stone, scissors, paper"

import random


def main():
    play_again_flag = 'y'
    while play_again_flag == 'y' or play_again_flag == 'Y' or play_again_flag == 'yes' or play_again_flag == 'YES':
        pc_choice = random.randint(1, 3)
        user_choice = get_user_choice()
        print_choice(pc_choice, 'Computer')
        print_choice(user_choice, 'You')
        game_result = check_winner(pc_choice, user_choice)
        if game_result == 1:
            print('Winner is computer!')
            play_again_flag = input('Want to play again (y/n)? ')
        elif game_result == 2:
            print('You win!')
            play_again_flag = input('Want to play again (y/n)? ')
        else:
            print('Draw!')
            play_again_flag = input('Want to play again (y/n)? ')
    print('Game over.')




# function to get choice from user
def get_user_choice():
    print('Choose one variant:')
    print('For stone press "1".')
    print('For scissors press "2".')
    print('For paper press "3".')
    continue_flag = 1 # declare variable for loop
    # loop to check user input
    while continue_flag == 1:
        user_input = input('Enter number (1-3): ')
        if user_input.isdigit():  # check if user inputed number
            user_choice = int(user_input)
            if user_choice == 1 or user_choice == 2 or user_choice == 3:
                continue_flag = 0
            else:
                print('Error, you should enter a number: 1, 2 or 3.')
        else:
            print('Error, you should enter a number: 1, 2 or 3.')
    return user_choice


def print_choice(number, name):
    if number == 1:
        print(f'{name} have chosen stone.')
    elif number == 2:
        print(f'{name} have chosen scissors.')
    else:
        print(f'{name} have chosen paper.')


# function check a winner, if winner is 1st choice, it returns 1, if second - 2. If draw - 0.
def check_winner(first_choice, second_choice):
    if first_choice == second_choice:
        return 0
    else:
        if first_choice == 1:
            if second_choice == 2:
                return 1
            else:
                return 2
        elif first_choice == 2:
            if second_choice == 1:
                return 2
            else:
                return 1
        else:
            if second_choice == 1:
                return 1
            else:
                return 2


main()
