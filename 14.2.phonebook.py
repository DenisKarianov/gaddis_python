# program to work with phonebook database
import sqlite3

# constants
MIN_CHOICE = 1
MAX_CHOICE = 5
ADD = 1
FIND = 2
CHANGE = 3
DELETE = 4
EXIT = 5
DB = 'phonebook.db'


def main():
    create_db()
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()
        if choice == ADD:
            add()
        elif choice == FIND:
            find()
        elif choice == CHANGE:
            change()
        elif choice == DELETE:
            delete()


def create_db():
    conn = None
    try:
        conn = sqlite3.Connection(DB)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Entries (Name TEXT, Phone TEXT''')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def display_menu():
    print("\n--- Phonebook ---")
    print("1. Add entry.")
    print("2. Find entry.")
    print("3. Change entry.")
    print("4. Delete entry.")
    print("5. Quit program.")


def get_menu_choice():
    loop_flag = 0
    while loop_flag < 2:
        choice = input("Enter your menu choice: ")
        if choice.isdigit():
            choice = int(choice)
            loop_flag += 1
            if MIN_CHOICE <= choice <= MAX_CHOICE:
                loop_flag += 1
            else:
                print(f"Your choice can be integer from {MIN_CHOICE} to {MAX_CHOICE} only.")
        else:
            print("Your choice can be a integer only.")
    return choice


def add():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        loop_flag = True
        while loop_flag:
            name = input("Enter a name: ")
            phone = input("Enter a phone number: ")
            cur.execute('''INSERT INTO Entries (Name, Phone)
                                VALUES (?, ?)''', (name, phone))
            conn.commit()
            print(f"Entry with name {name} and phone number {phone} was added.")
            again = input("Add one more entry (y/n)?")
            if again.lower() != 'y':
                loop_flag = False
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def find():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        search = input("Enter a name or phone number to find: ")
        cur.execute('''SELECT Name, Phone FROM Entries WHERE Name LIKE "%?%" or Phone LIKE "%?%"''', (search, search))
        result = cur.fetchall()
        if len(result) > 0:
            # variables to print header
            n = 'Name'
            ph = 'Phone'
            print(f"{n:<10} {ph:<12}")
            print("----------------------")
            for entry in result:
                print(f"{entry[0]:<10} {entry[1]:<12}")
        else:
            print("Entry not found.")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def change():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        search = input("Enter a name or phone number to change: ")
        cur.execute('''SELECT RowID, Name, Phone FROM Entries WHERE Name LIKE "%?%" or Phone LIKE "%?%"''',
                    (search, search))
        if

    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def most_city():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('''SELECT MAX(Population) FROM Cities''')
        max_pop = cur.fetchone()[0]
        cur.execute('''SELECT CityName FROM Cities WHERE Population == ?''', (max_pop,))
        print(f"Most populated city: {cur.fetchone()[0]}")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


def least_city():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('''SELECT MIN(Population) FROM Cities''')
        min_pop = cur.fetchone()[0]
        cur.execute('''SELECT CityName FROM Cities WHERE Population == ?''', (min_pop,))
        print(f"Least populated city: {cur.fetchone()[0]}")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()
