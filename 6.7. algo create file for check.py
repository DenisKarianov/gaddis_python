# program opens file, use a loop to write to a file numbers 1-100 and close file.


def main():
    output_file = open('students.txt', 'w')  # open a file for writing
    output_file.write('Denis\n')
    output_file.write('5\n')
    output_file.write('John Perc\n')
    output_file.write('4\n')
    output_file.write('Jack Bauer\n')
    output_file.write('7\n')
    output_file.write('Chuck Norris\n')
    output_file.write('777\n')
    output_file.write('Julia Milan\n')
    output_file.write('4\n')
    output_file.close()


main()
