# program to change field in entry from a file.

import os

# global constants
ENTRY_TO_CHANGE = 'Julia Milan'
NEW_GRADE = '100'


def main():
    students_file = open('students.txt', 'r')  # open a file for reading
    temp_file = open('temp.txt', 'w')  # open a file for writing
    student_name = students_file.readline()  # first reading for student's name
    found = False  # declare a flag variable
    while student_name != '':
        student_grade = students_file.readline()  # read student's grade
        student_name = student_name.rstrip('\n')  # remove \n for correct compare
        # if it's not an entry for removal, write them to temp file
        if student_name == ENTRY_TO_CHANGE:
            found = True
            temp_file.write(f'{student_name}\n')
            temp_file.write(f'{NEW_GRADE}\n')  # no need to add \n, because it already is
        else:
            temp_file.write(f'{student_name}\n')
            temp_file.write(student_grade)
        student_name = students_file.readline()  # read next line for next student's name
    students_file.close()
    temp_file.close()
    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')
    if found:
        print(f"Entry {ENTRY_TO_CHANGE} was changed.")
    else:
        print(f"Entry {ENTRY_TO_CHANGE} wasn't found.")


main()
