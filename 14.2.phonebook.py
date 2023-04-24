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
        cur.execute('''CREATE TABLE IF NOT EXISTS Entries (Name TEXT, Phone TEXT)''')
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
        search = '%' + search.lower() + '%'
        cur.execute('''SELECT Name, Phone FROM Entries WHERE lower(Name) LIKE ? OR
                    lower(Phone) LIKE ?''', (search, search))
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
        search = '%' + search.lower() + '%'
        cur.execute('''SELECT RowID, Name, Phone FROM Entries WHERE lower(Name) LIKE ? or lower(Phone) LIKE ?''',
                    (search, search))
        result = cur.fetchall()
        if len(result) > 0:
            display_entry(result)
        if len(result) == 1:
            update_entry(cur, search)
            conn.commit()
        elif len(result) > 1:  # if there were more than one entry found
            loop_flag = 0
            while loop_flag < 2:
                id = input("Enter entry's RowID that need to be change: ")
                if id.isdigit():
                    id = int(id)
                    loop_flag += 1
                    # check if entered RowID is in table
                    cur.execute('''SELECT RowID FROM Entries WHERE RowID == ?''', (id,))
                    result_id = cur.fetchall()
                    if len(result_id) == 1:  # found one RowID, that user has entered
                        loop_flag += 1
                        name = input("Enter new name or just press 'Enter' to save previous name: ")
                        phone = input("Enter new phone number or just press 'Enter' to save previous phone number: ")
                        if len(name) > 1:
                            cur.execute('''UPDATE Entries SET Name = ?
                                       WHERE RowID == ?''', (name, id))
                            print(f"{name} was added.")
                        if len(phone) > 1:
                            cur.execute('''UPDATE Entries SET Phone = ?
                                       WHERE RowID == ?''', (phone, id))
                            print(f"{phone} was added.")
                        conn.commit()
                    else:
                        print("Wrong RowID.")
                else:
                    print("RowID should be a integer.")
        else:
            print("Entry was not found.")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def delete():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        search = input("Enter a name or phone number to delete: ")
        search = '%' + search.lower() + '%'
        cur.execute('''SELECT RowID, Name, Phone FROM Entries WHERE lower(Name) LIKE ? or lower(Phone) LIKE ?''',
                    (search, search))
        result = cur.fetchall()
        if len(result) > 0:
            display_entry(result)
            loop_flag = 0
            while loop_flag < 2:
                id = input("Enter entry's RowID to delete: ")
                if id.isdigit():
                    id = int(id)
                    loop_flag += 1
                    # check if entered RowID is in table
                    cur.execute('''SELECT RowID FROM Entries WHERE RowID == ?''', (id,))
                    result_id = cur.fetchall()
                    if len(result_id) == 1:  # found one RowID, that user has entered
                        loop_flag += 1
                        cur.execute('''DELETE FROM Entries WHERE RowID == ?''', (id,))
                        print("Entry was deleted.")
                        conn.commit()
                    else:
                        print("Wrong RowID.")
                else:
                    print("RowID should be a integer.")
            conn.commit()
        else:
            print("Entry was not found.")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def display_entry(result):
    # variables to print header
    id = 'RowID'
    n = 'Name'
    ph = 'Phone'
    print(f"{id:<5} {n:<10} {ph:<12}")
    print("----------------------")
    for entry in result:
        print(f"{entry[0]:<5} {entry[1]:<10} {entry[2]:<12}")


def update_entry(cur, search):
    name = input("Enter new name or just press 'Enter' to save previous name: ")
    phone = input("Enter new phone number or just press 'Enter' to save previous phone number: ")
    search = '%' + search.lower() + '%'
    if len(name) > 1:
        cur.execute('''UPDATE Entries SET Name = ?
                   WHERE lower(Name) LIKE ? or lower(Phone) LIKE ?''', (name, search, search))
        print(f"{name} was added.")
    if len(phone) > 1:
        cur.execute('''UPDATE Entries SET Phone = ?
                   WHERE lower(Name) LIKE ? or lower(Phone) LIKE ?''', (phone, search, search))
        print(f"{phone} was added.")


if __name__ == '__main__':
    main()
