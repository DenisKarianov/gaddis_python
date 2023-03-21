# program to get data from txt-file about winners of world series and let user find this data

# global constants
TEXTFILE = 'WorldSeriesWinners2.txt'


def main():
    team_wins, years_team = make_dict(TEXTFILE)  # make necessary dictionaries
    user_year = int(input("Enter a year: "))
    if user_year in years_team:
        print(f"In {user_year} won {years_team[user_year]}. {years_team[user_year]} has {team_wins[years_team[user_year]]} wins"
              f" in WorldSeries from 1903 till 2009.")
    else:
        print(f"There is no data for year {user_year}.")



def rstrip_list(list):
    index = 0
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    return list


def make_dict(txtfile):
    # open file
    try:
        infile = open(txtfile, "r")
        winners_list = infile.readlines()
        infile.close()
        # remove \N
        winners_list = rstrip_list(winners_list)
        # make dict, where key - team name, value - wins' quantity
        team_wins = {}
        for t in set(winners_list):
            if not t.startswith('World Series'):  # exclude years, where wasn't games
                team_wins[t] = winners_list.count(t)
        # make dict, where key - year, value - winning team
        years_team = {}
        for i, t in enumerate(winners_list, start=1903):
            if not t.startswith('World Series'):
                years_team[i] = t
        return team_wins, years_team
    except FileNotFoundError:
        print(f"File {txtfile} is not found.")

# Call the main function.
if __name__ == '__main__':
    main()
