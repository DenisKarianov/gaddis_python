# program opens file my_name.txt, write a name to it and close it.


def main():
    output_file = open('my_name.txt', 'w') # open a file for writing
    output_file.write('Denis')
    output_file.close()


main()
