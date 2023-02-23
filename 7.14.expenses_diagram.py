# program to make diagram for expenses from data from file

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# global constants
FILE_NAME = 'expenses.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        data_list = infile.readlines()
        infile.close()
        # transform list's elements to float
        index = 0
        while index < len(data_list):
            data_list[index] = float(data_list[index])
            index += 1
        # create labels' list
        labels_list = ['rent', 'transport', 'food', 'clothes', 'other']
        # create diagram
        plt.pie(data_list, labels=labels_list)
        # create header
        plt.title('Expenses')
        # show diagram
        plt.show()
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


# Call the main function.
if __name__ == '__main__':
    main()
