# program to count average word quantity in line from data in file

# global constants
FILE_NAME = 'text.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        sentence_list = infile.readlines()
        infile.close()
        # declare a variable to count quantity of words
        word_total = 0
        for sent in sentence_list:
            word_total += len(sent.split())
        print(f'Average word quantity in one sentence: {word_total / len(sentence_list):.1f}')
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')

    # Call the main function.


if __name__ == '__main__':
    main()
