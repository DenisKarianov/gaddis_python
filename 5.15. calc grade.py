# count average grade and letter grade
def calc_average(grade1, grade2, grade3, grade4, grade5):
    average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
    return average_grade


def determine_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80 and grade <= 89:
        return 'B'
    elif grade >= 70 and grade <= 79:
        return 'C'
    elif grade >= 60 and grade <= 69:
        return 'D'
    else:
        return 'F'


def main():
    # get value of five grades from user
    grade1 = int(input('Enter your first grade: '))
    grade2 = int(input('Enter your second grade: '))
    grade3 = int(input('Enter your third grade: '))
    grade4 = int(input('Enter your fourth grade: '))
    grade5 = int(input('Enter your fifth grade: '))

    # get and print average grade
    average_grade = calc_average(grade1, grade2, grade3, grade4, grade5)
    print(f'Your average grade is {average_grade}.')

    # get and print letter grades
    print(f"Letter grade of your first grade {grade1} is {determine_grade(grade1)}.")
    print(f"Letter grade of your second grade {grade2} is {determine_grade(grade2)}.")
    print(f"Letter grade of your third grade {grade3} is {determine_grade(grade3)}.")
    print(f"Letter grade of your fourth grade {grade4} is {determine_grade(grade4)}.")
    print(f"Letter grade of your fifth grade {grade5} is {determine_grade(grade5)}.")




main()
