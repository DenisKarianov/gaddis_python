# program to answer like magic ball

import random

# global constants
FILE_NAME = '8_ball_responses_ru.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        answers_list = infile.readlines()
        infile.close()
        # remove \N
        answers_list = rstrip_list(answers_list)
        # declare loop variable
        loop_flag = 'д'
        while loop_flag == 'д' or loop_flag == 'Д':
            # get question from user
            question = input("Пожалуйста, введите вопрос: ")
            # print random answer from answers' list
            print(f"{random.choice(answers_list)}")
            loop_flag = input("Ещё вопрос(y/n)? ")
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
