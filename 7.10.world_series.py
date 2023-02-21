# program to check winners from data in file

# global constants
FILE_NAME = 'WorldSeriesWinners.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        winners_list = infile.readlines()
        infile.close()
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')
    # remove \N
    winners_list = rstrip_list(winners_list)
    # get team's name from user
    search_team = input("Please, enter a team's name: ")
    # make list of searched team's name for quantity of win years
    found_list = [item for item in winners_list if item == search_team]
    if len(found_list) > 0:
        print(f"{search_team} won {len(found_list)} times.")
    else:
        print(f"{search_team} didn't win.")

def rstrip_list(list):
    index = 0
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    return list



# Call the main function.
if __name__ == '__main__':
    main()
