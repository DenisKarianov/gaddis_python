# program to work with students' database
import sqlite3

# constants
MIN_CHOICE = 1
MAX_CHOICE = 6
ADD = 1
FIND = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
EXIT = 6

MAIN_MIN_CHOICE = 1
MAIN_MAX_CHOICE = 4
MAIN_MAJORS = 1
MAIN_DEPS = 2
MAIN_STUDENTS = 3
MAIN_EXIT = 4
DB = 'student_info.db'


def main():
    create_db()
    choice = 0
    while choice != MAIN_EXIT:
        display_main_menu()
        choice = get_menu_choice(MAIN_MIN_CHOICE, MAIN_MAX_CHOICE)
        if choice == MAIN_MAJORS:
            choice = 0
            display_menu("Majors")
            choice = get_menu_choice(MIN_CHOICE, MAX_CHOICE)
            while choice != EXIT:
                if choice == ADD:
                    add(0)
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
        cur.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY NOT NULL, Name TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY NOT NULL, Name TEXT)''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY NOT NULL, Name TEXT,
                    MajorID INTEGER, DeptID INTEGER, FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))''')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


def display_main_menu():
    print("\n--- Database management ---")
    print("1. Majors.")
    print("2. Departments.")
    print("3. Students.")
    print("4. Quit program.")


def display_menu(db_name):
    print(f"\n--- {db_name} ---")
    print("1. Add entry.")
    print("2. Find entry.")
    print("3. Change entry.")
    print("4. Delete entry.")
    print("5. Show all entries.")
    print("6. Exit to previous menu.")


def get_menu_choice(min_choice, max_choice):
    loop_flag = 0
    while loop_flag < 2:
        choice = input("Enter your menu choice: ")
        if choice.isdigit():
            choice = int(choice)
            loop_flag += 1
            if min_choice <= choice <= max_choice:
                loop_flag += 1
            else:
                print(f"Your choice can be integer from {min_choice} to {max_choice} only.")
        else:
            print("Your choice can be a integer only.")
    return choice


# mode: 0 Majors, 1 Departments, 2 Students
def add(mode):
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')  # turn on foreign keys support
        if mode == 0:
            name = input("Enter major's name: ")
            cur.execute('''INSERT INTO Majors (Name) VALUES (?)''', (name,))
            conn.commit()
            print(f"Entry with name {name} was added.")
        elif mode == 1:
            name = input("Enter department's name: ")
            cur.execute('''INSERT INTO Departments (Name) VALUES (?)''', (name,))
            conn.commit()
            print(f"Entry with name {name} was added.")
        elif mode == 2:
            name = input("Enter student's name: ")
            # validation loop for integer MajorID
            loop_flag = True
            while loop_flag:
                majorid = input("Enter student's MajorID: ")
                if majorid.isdigit():
                    majorid = int(majorid)
                    loop_flag = False
            # validation loop for integer DeptID
            loop_flag = True
            while loop_flag:
                deptid = input("Enter student's DeptID: ")
                if deptid.isdigit():
                    deptid = int(deptid)
                    loop_flag = False
            cur.execute('''INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)''', (name, majorid, deptid))
            conn.commit()
            print(f"Student with name {name} was added.")
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
        # check quantity of columns in table to
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
