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
        index_data = {}  # make empty dictionary
        for w in words:
            if w != '':  # exclude empty string from selection
                index_data[w] = get_list(w, infile_list)  # add to dict word as key and list of lines' numbers as value
        # write index data to file, every line - word : lines' numbers, words are sorted by alphabet
        outfile = open("index.txt", "w")
        keys_list = list(index_data.keys())  # get keys' list
        keys_list.sort()  # sort list
        for word in keys_list:
            numbers_write = ''  # make empty string to write numbers to write to file
            for i, n in enumerate(index_data[word]):
                numbers_write += str(n)
                if i < len(index_data[word]) - 1:  # add space between numbers except after last number
                    numbers_write += ' '
            outfile.write(f"{word}: {numbers_write}\n")
        outfile.close()
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
        if word in line.lower():
            outlist.append(i + 1)  # add number of line
    return outlist


# Call the main function.
if __name__ == '__main__':
    main()
