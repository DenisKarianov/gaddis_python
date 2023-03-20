# program to find unique words in txt-file

# global constants
TEXTFILE = 'peresolil.txt'


def main():
    # open file
    try:
        infile = open(TEXTFILE, "r")
        txt_str = infile.read()
        infile.close()
        txt_str = txt_str.rstrip("\n")
        words_list = txt_str.split()  # make words' list from string
        words_set = set(words_list)  # make set from list to remove non-unique words
        print(words_set)
    except FileNotFoundError:
        print(f"File {TEXTFILE} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
