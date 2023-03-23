# program to make word index for txt-file

import re  # to remove punctuation marks

# global constants
TEXTFILE = 'declaration.txt'


def main():
    try:
        infile = open(TEXTFILE, "r")
        infile_list = infile.readlines()
        infile.close()
        # make words' list
        words = get_words(infile_list)
        # make dictionary, key - word, value - list of lines' number, where there's this word
        index_data = {}  # empty dictionary
        for w in words:
            index_data[w] = get_list(w, infile_list)




    except FileNotFoundError:
        print(f"File {TEXTFILE} is not found.")


def get_words(inlist):
    for i, v in enumerate(inlist):
        inlist[i] = inlist[i].rstrip('\n')
    # get words from lines
    words = []  # empty list for words
    for line in inlist:
        for word in line.split():  # split line by spaces
            words.append(word)  # add word to words list
    # remove punctuation marks and make lowercase
    for i, w in enumerate(words):
        words[i] = re.sub(r'[^\w\s]', '', words[i])
        words[i] = words[i].lower()
    # make set to stay only unique words
    words = set(words)
    return words

# function to get list of lines' number, where there's this word in some list
def get_list(word, inlist):
    outlist = []  # empty list of lines' numbers
    for i, line in enumerate(inlist):
        if word in line:
            outlist.append(i + 1)
    return outlist

# Call the main function.
if __name__ == '__main__':
    main()
