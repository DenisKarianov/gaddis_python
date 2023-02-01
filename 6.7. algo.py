# program to delete entry from a file.

import os

# global constants
ENTRY_FOR_REMOVE = 'John Perc'


def main():
    students_file = open('students.txt', 'r')  # open a file for reading
    temp_file = open('temp.txt', 'w')  # open a file for writing
    student_name = students_file.readline()  # first reading for student's name
    found = False  # declare a flag variable
    while student_name != '':
        student_grade = students_file.readline()  # read student's grade
        student_name = student_name.rstrip('\n')
        # if it's not an entry for removal, write them to temp file
        if student_name != ENTRY_FOR_REMOVE:
            temp_file.write(f'{student_name}\n')
            temp_file.write(student_grade)  # no need to add \n, because it already is
        else:
            found = True
        student_name = students_file.readline()  # read next line for next student's name
    students_file.close()
    temp_file.close()
    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')
    if found:
        print(f"Entry {ENTRY_FOR_REMOVE} was deleted.")
    else:
        print(f"Entry {ENTRY_FOR_REMOVE} wasn't found.")


main()
