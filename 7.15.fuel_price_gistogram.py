# program to make diagram for weekly fuel prices in 1994
# from data from file

import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# set up window's size
fig, ax = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')

# global constants
FILE_NAME = '1994_Weekly_Gas_Averages.txt'


def main():
    try:
        # read data from file to list
        infile = open(FILE_NAME, 'r')
        fuel_list = infile.readlines()
        infile.close()
        # transform list's elements to float
        index = 0
        while index < len(fuel_list):
            fuel_list[index] = float(fuel_list[index])
            index += 1
        # create list for left edges of columns
        left_edges = []
        for i in range(0, 104, 2):
            left_edges.append(i)
        # create diagram
        plt.bar(left_edges, fuel_list, 1.5)
        # create header
        plt.title('Week fuel prices in 1994')
        # axis labels
        plt.xlabel('Weeks')
        plt.ylabel('USD')
        # divider labels
        xtick_coord = []
        for i in range(0, 104, 2):
            xtick_coord.append(i)
        xtick_labels = []
        for i in range(1, 53):
            xtick_labels.append(i)
        plt.xticks(xtick_coord, xtick_labels)
        # change height of y-axis
        plt.ylim(ymin=0.0, ymax=1.5)
        # show diagram
        plt.show()
    except FileNotFoundError:
        print(f'No such file or directory: {FILE_NAME}.')


# Call the main function.
if __name__ == '__main__':
    main()
