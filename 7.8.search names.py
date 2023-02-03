# program for search names in files

# global constants
GIRL_NAMES_FILE = 'GirlNames.txt'
BOY_NAMES_FILE = 'BoyNames.txt'


def main():
    try:
        # read girl names from file to list
        girl_infile = open(GIRL_NAMES_FILE, 'r')
        girl_name_list = girl_infile.readlines()
        girl_infile.close()
        boy_infile = open(BOY_NAMES_FILE, 'r')
        boy_name_list = boy_infile.readlines()
        boy_infile.close()
    except FileNotFoundError:
        print('No such file or directory.')
    # remove '\n' from girl names list
    index = 0
    while index < len(girl_name_list):
        girl_name_list[index] = girl_name_list[index].rstrip('\n')
        index += 1
    # remove '\n' from boy names list
    index = 0
    while index < len(boy_name_list):
        boy_name_list[index] = boy_name_list[index].rstrip('\n')
        index += 1
    # get names for search from user
    girl_name_search = input("Enter a girl's name or 'n',"
                             "if you don't have a girl's name: ")
    boy_name_search = input("Enter a boy's name or 'n',"
                            "if you don't have a boy's name: ")
    # check if names in lists
    if girl_name_search != 'n' and girl_name_search != 'N':
        girl_search_flag = True  # set up flag that girl's name was searched
        if girl_name_search in girl_name_list:
            girl_name_found = True  # set up flag for girl's name
        else:
            girl_name_found = False  # set up flag for girl's name
    else:
        girl_search_flag = False  # set up flag that girl's name wasn't searched
    if boy_name_search != 'n' and boy_name_search != 'N':
        boy_search_flag = True  # set up flag that boy's name was searched
        if boy_name_search in boy_name_list:
            boy_name_found = True  # set up flag for boy's name
        else:
            boy_name_found = False  # set up flag for boy's name
    else:
        boy_search_flag = False  # set up flag that boy's name wasn't searched
    # print if names in popular names list
    if girl_search_flag:
        if girl_name_found:
            print(f"{girl_name_search} is in popular girl's names list.")
        else:
            print(f"{girl_name_search} is not in popular girl's names list.")
    if boy_search_flag:
        if boy_name_found:
            print(f"{boy_name_search} is in popular boy's names list.")
        else:
            print(f"{boy_name_search} is not in popular boy's names list.")


# Call the main function.
if __name__ == '__main__':
    main()
