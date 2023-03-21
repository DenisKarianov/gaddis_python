# program to make dictionary with data about words' frequency in txt-file

# global constants
TEXTFILE1 = 'peresolil.txt'
TEXTFILE2 = 'tolstii.txt'


def main():
    # open files
    try:
        infile = open(TEXTFILE1, "r")
        txt_str1 = infile.read()
        infile.close()
        txt_str1 = txt_str1.rstrip("\n")
        try:
            infile2 = open(TEXTFILE2, "r")
            txt_str2 = infile2.read()
            infile2.close()
            txt_str2 = txt_str2.rstrip("\n")
            # print unique words from both files
            words_list1 = txt_str1.split()  # make words' list from string
            words_list2 = txt_str2.split()  # make words' list from string
            # make words' set to get unique words
            set1 = set(words_list1)
            set2 = set(words_list2)
            un_set = set1 | set2  # unified set to get unique words in both sets
            print("Unique words in both files.")
            for word in un_set:
                print(word, end=' ')
            # get words, included in both files
            print()
            print("Words, included in both files.")
            for word in set1 & set2:
                print(word, end=' ')
            print()
            print(f"Words, included in {TEXTFILE1} file, but not included in {TEXTFILE2}.")
            for word in set1 - set2:
                print(word, end=' ')
            print()
            print(f"Words, included in {TEXTFILE2} file, but not included in {TEXTFILE1}.")
            for word in set2 - set1:
                print(word, end=' ')
            print()
            print("Words, included only in one file, but not in both.")
            for word in set2 ^ set1:
                print(word, end=' ')


        except FileNotFoundError:
            print(f"File {TEXTFILE1} is not found.")
    except FileNotFoundError:
        print(f"File {TEXTFILE1} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
