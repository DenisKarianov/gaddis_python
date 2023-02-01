# program opens a output file, but doesn't erase it's content.


def main():
    input_file = open('number_list.txt', 'a') # open a file for writing
    input_file.close()


main()
