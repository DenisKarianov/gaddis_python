# program read in file names and scores of golf players and print it.

# global constants
FILE_NAME = 'golf.txt'

def main():
    input_file = open(FILE_NAME, 'r')  # open a file for reading
    counter = 0  # declare variable for define names and scores
    for line in input_file:
        counter += 1
        if counter % 2 != 0:
            name = line.rstrip('\n')
            print(f"Player's name: {name}")
        else:
            print(f"Player's score: {line}")
    input_file.close()


main()
