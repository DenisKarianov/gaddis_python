# program to make dictionary for encoding characters

import pickle

# global constants for menu items
FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
# for data file's name
DATA_FILE = 'names_emails.dat'


def main():
    try:
        data_file = open(DATA_FILE, 'rb')  # try to open dictionary file
        try:
            names_emails = pickle.load(data_file)
            data_file.close()
        except EOFError:  # if there's no saved data
            data_file.close()
            names_emails = {}
    except FileNotFoundError:  # if there's no data file
        names_emails = {}
    choice = 0  # variable for user's menu item's choice
    while choice != QUIT:
        choice = get_menu_choice()  # get menu item from user
        # realise chosen item
        if choice == 1:
            find(names_emails)
        elif choice == 2:
            add(names_emails)
        elif choice == 3:
            change(names_emails)
        elif choice == 4:
            delete(names_emails)
    # save data to file to quit program
    output_file = open(DATA_FILE, 'wb')
    pickle.dump(names_emails, output_file)
    output_file.close()
    print("All data was saved successfully.")


def get_menu_choice():
    print()
    print("Names and emails")
    print("-------------------")
    print("1. Find email by name")
    print("2. Add new name and email")
    print("3. Change name and email")
    print("4. Delete name and email")
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
    name = input("Enter name to find: ")
    print(f'Email: {dict1.get(name, "Not found.")}')


def add(dict1):
    name = input("Enter name to add: ")
    email = input("Enter email to add: ")
    if name not in dict1:
        dict1[name] = email
        print(f"Entry {name} and {email} was added.")
    else:
        print("This entry already exists.")


def change(dict1):
    name = input("Enter name to change: ")
    if name in dict1:
        email = input("Enter email: ")
        dict1[name] = email
        print(f"Entry {name} and {email} was changed.")
    else:
        print(f"{name} is not found.")


def delete(dict1):
    name = input("Enter name: ")
    if name in dict1:
        del dict1[name]
        print(f"Entry {name} was deleted.")
    else:
        print(f"{name} is not found.")


# Call the main function.
if __name__ == '__main__':
    main()
