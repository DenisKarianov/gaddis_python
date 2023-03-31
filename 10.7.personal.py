# program to create an object from class Employee

import employee
import pickle

# global constants for menu items
FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
# for data file's name
DATA_FILE = 'personal.dat'


def main():
    # make dictionary
    personal = load_personal()
    choice = 0  # variable for user's menu item's choice
    while choice != QUIT:
        choice = get_menu_choice()  # get menu item from user
        # realise chosen item
        if choice == 1:
            find(personal)
        elif choice == 2:
            add(personal)
        elif choice == 3:
            change(personal)
        elif choice == 4:
            delete(personal)
    # save data to file to quit program
    output_file = open(DATA_FILE, 'wb')
    pickle.dump(personal, output_file)
    output_file.close()
    print("All data was saved successfully.")

def load_personal():
    try:
        data_file = open(DATA_FILE, 'rb')  # try to open dictionary file
        try:
            personal = pickle.load(data_file)
            data_file.close()
        except EOFError:  # if there's no saved data
            data_file.close()
            personal = {}
    except FileNotFoundError:  # if there's no data file
        personal = {}
    return personal
def get_menu_choice():
    print()
    print("Menu")
    print("-------------------")
    print("1. Find employee")
    print("2. Add new employee")
    print("3. Change employee")
    print("4. Delete employee")
    print("5. Quit")
    print()
    # get item from user and validate it
    loop_flag = 0  # variable for loop control
    while loop_flag < 2:
        loop_flag = 0  # erase for new iteration
        # get menu item from user
        choice = input("Enter chosen menu item: ")
        if choice.isdigit():
            loop_flag += 1
            choice_int = int(choice)
            if 1 <= choice_int <= 5:
                loop_flag += 1
    return choice_int


def find(dict1):
    number = int(input("Enter employee's number to find: "))
    try:
        print(dict1[number])
    except KeyError:
        print("The employee not found.")


def add(dict1):
    number = int(input("Enter employee's number to add: "))
    if number not in dict1:
        name = input("Enter employee's name to add: ")
        depart = input("Enter employee's department to add: ")
        position = input("Enter employee's position to add: ")
        emp1 = employee.Employee(name, number, depart, position)
        dict1[number] = emp1
        print("Employee's entry was added.")
    else:
        print("This entry already exists.")


def change(dict1):
    number = input("Enter employee's number to change: ")
    if number in dict1:
        was_changed = False  # flag to control changes
        old_entry = dict1[number]  # make entry before changes
        print("Enter new data. If no need to change certain data - just press 'Enter'.")
        in_number = input("Enter new number: ")
        end_flag = False  # flag to validate number
        while not end_flag:
            if in_number.isdigit():
                in_number = int(in_number)
                was_changed = True
                end_flag = True
            elif in_number == '':
                in_number = old_entry.get_number()  # get old number for new entry, that will change
                end_flag = True
            else:
                in_number = input("Enter new number, it should be digit: ")
        in_name = input("Enter new name: ")
        if in_name != '':
            was_changed = True
        else:
            in_name = old_entry.get_name()  # get old name for new entry, that will change
        in_depart = input("Enter new department: ")
        if in_depart != '':
            was_changed = True
        else:
            in_depart = old_entry.get_depart()  # get old department for new entry, that will change
        in_position = input("Enter new position: ")
        if in_position != '':
            was_changed = True
        else:
            in_position = old_entry.get_position()
        emp = employee.Employee(in_name, in_number, in_depart, in_position)  # make new entry
        dict1[in_number] = emp  # replace old entry with new one
        if was_changed:
            print("Entry was changed.")
        else:
            print("Entry was not changed.")
    else:
        print("Employee not found.")


def delete(dict1):
    number = input("Enter employee's number to delete: ")
    if number in dict1:
        del dict1[number]
        print(f"Entry number {number} was deleted.")
    else:
        print(f"{number} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
