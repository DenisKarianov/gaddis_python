# program to answer like magic ball

import random

# global constants
FILE_NAME = '8_ball_responses.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        answers_list = infile.readlines()
        infile.close()
        # remove \N
        answers_list = rstrip_list(answers_list)
        # declare loop variable
        loop_flag = 'y'
        while loop_flag == 'y' or loop_flag == 'Y':
            # get question from user
            question = input("Please, enter your question: ")
            # print random answer from answers' list
            print(f"{random.choice(answers_list)}")
            loop_flag = input("Want to ask again(y/n)? ")
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


def rstrip_list(list):
    index = 0
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    return list


# Call the main function.
if __name__ == '__main__':
    main()
