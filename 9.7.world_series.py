# program to get data from txt-file about winners of world series and let user find this data

# global constants
TEXTFILE = 'WorldSeriesWinners2.txt'


def main():
    # open file
    try:
        infile = open(TEXTFILE, "r")
        winners_list = infile.readlines()
        infile.close()
        # remove \N
        winners_list = rstrip_list(winners_list)
        # make dict, where key - team name, value - wins' quantity
        team_wins = {}
        for t in set(winners_list):
            if not t.startswith('World Series'):  # exclude years, where wasn't games
                team_wins[t] = winners_list.count(t)
        print(team_wins)
        # make dict, where key - year, value - winning team
        years_team = {}
        for i, t in enumerate(winners_list, start=1903):
            if not t.startswith('World Series'):
                years_team[i] = t
        print(years_team)



    except FileNotFoundError:
        print(f"File {TEXTFILE} is not found.")


def rstrip_list(list):
    index = 0
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    return list


# Call the main function.
if __name__ == '__main__':
    main()
