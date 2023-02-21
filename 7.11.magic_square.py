# program to check if 2d-list is magic square Lo Shu


def main():
    # create 2d-list for test
    check_list = [[4, 3, 8], [9, 2, 1], [9, 5, 1]]
    check_list_loshu(check_list)


# create function for checking list for Lo Shu magic
def check_list_loshu(some_list):
    # check if list's length is 3
    if len(some_list) == 3:
        # check if list is 2d
        if all([type(x) is list for x in some_list]):
            # check if nested lists' length is 3
            if all([len(i) == 3 for i in some_list]):
                # check if all numbers is integer numbers from 1 to 9
                int_flag = 0
                for row in some_list:
                    for number in row:
                        if not isinstance(number, int) or number < 1 or number > 9:
                            int_flag += 1
                if int_flag == 0:
                    # check of sums of all rows, columns and diagonals are even
                    results_list = []
                    results_list.append(some_list[0][0] + some_list[0][1] + some_list[0][2])
                    results_list.append(some_list[1][0] + some_list[1][1] + some_list[1][2])
                    results_list.append(some_list[2][0] + some_list[2][1] + some_list[2][2])
                    results_list.append(some_list[0][0] + some_list[1][0] + some_list[2][0])
                    results_list.append(some_list[0][1] + some_list[1][1] + some_list[2][1])
                    results_list.append(some_list[0][2] + some_list[1][2] + some_list[2][2])
                    results_list.append(some_list[0][0] + some_list[1][1] + some_list[2][2])
                    results_list.append(some_list[2][0] + some_list[1][1] + some_list[0][2])
                    if all(x == results_list[0] for x in results_list):
                        print("It's a magic square!")
                    else:
                        print(
                            "It's not a magic square, because all rows, columns and diagonals should have even sums.")
                else:
                    print("It's not a magic square, because magic square should have only integer numbers from 1 to 9.")

            else:
                print("It's not a magic square, because it has not 3 columns in each row .")
        else:
            print("It's not a magic square, because it has not columns.")
    else:
        print("It's not a magic square, because it has not a 3 rows.")


# Call the main function.
if __name__ == '__main__':
    main()
