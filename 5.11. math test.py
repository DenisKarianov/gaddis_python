# math test program

import random

# global constants
MIN_NUMBER = 1
MAX_NUMBER = 500


def main():
    # call function to generate two random numbers
    first_number, second_number = generate_2_random_numbers(MIN_NUMBER, MAX_NUMBER)

    # print a task
    print('Calculate the sum of two numbers:')
    print(f'{first_number}')
    print(f'+ {second_number}')

    # ask user for input answer
    user_answer = float(input('Please, input the sum of two numbers: '))

    # call for control correct function and print result
    if is_correct(first_number, second_number, user_answer):
        print('Congratulations, your answer is correct!')
    else:
        print(f'Your answer is wrong. Correct answer is {first_number + second_number}!')


def generate_2_random_numbers(min, max):
    first_number = random.randint(min, max)
    second_number = random.randint(min, max)
    return first_number, second_number


def is_correct(first_number, second_number, answer):
    if first_number + second_number == answer:
        status = True
    else:
        status = False
    return status


main()
