# program to count words frequency in txt-file

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
        words_freq = {}  # dict for save data about words frequency
        for word in words_list:
            words_freq[word] = words_list.count(word)
        # variables for table
        w = "Word"
        freq = "Frequency"
        print(f"{w:^15}\t{freq:^9}")
        for word in words_freq:
            print(f"{word:^15}\t{words_freq[word]:^9}")
    except FileNotFoundError:
        print(f"File {TEXTFILE} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
