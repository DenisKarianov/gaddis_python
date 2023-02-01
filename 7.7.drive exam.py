# program for drive lisence exam

# global constants
MIN_PASS_EXAM_NUMBER = 15
USER_ANSWERS_FILE = 'student_solution.txt'


def main():
    # make a list of correct answers
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D',
                       'A']
    try:
        infile = open(USER_ANSWERS_FILE, 'r')
        user_answers = infile.readlines()  # file content to list
        infile.close()
    except FileNotFoundError:
        print(f'No such file or directory: {USER_ANSWERS_FILE}')
    # remove '\n'
    index = 0
    while index < len(user_answers):
        user_answers[index] = user_answers[index].rstrip('\n')
        index += 1
    # declare a variable to count correct answers
    correct_answers_counter = 0
    # create a list for wrong answers numbers
    wrong_answers_numbers = []
    # compare lists with correct answers and user answers, count correct answers
    # and save in list numbers of wrong answers
    index = 0
    while index < len(correct_answers):
        if correct_answers[index] == user_answers[index]:
            correct_answers_counter += 1
        else:
            wrong_answers_numbers.append(index + 1)
        index += 1
    # check if exam is passed and print message
    if correct_answers_counter >= MIN_PASS_EXAM_NUMBER:
        print('You have passed the exam!')
    else:
        print('You have not passed the exam!')
    print(f'Correct answers quantity: {correct_answers_counter}')
    print(f'Wrong answers quantity: {len(correct_answers) - correct_answers_counter}')
    if len(correct_answers) - correct_answers_counter == 0:
        print('All answers are correct!')
    else:
        print('Wrong answers numbers:')
        for number in wrong_answers_numbers:
            print(number)


# Call the main function.
if __name__ == '__main__':
    main()
