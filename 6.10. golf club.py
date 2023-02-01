# program writes names and scores of golf players and write them to file.

# global constants
FILE_NAME = 'golf.txt'

def main():
    continue_flag = 'y'  # declare variable for loop control by user
    output_file = open(FILE_NAME, 'w')  # open a file for writing
    while continue_flag == 'y' or continue_flag == 'Y':
        player_name = input("Enter a player's name: ")
        player_score = input("Enter a player's score: ")
        output_file.write(f'{player_name}\n')
        output_file.write(f'{player_score}\n')
        continue_flag = input('Would you like to enter a data for another player(y/n)? ')
    output_file.close()


main()
