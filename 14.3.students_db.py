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
            while choice != EXIT:
                display_menu("Majors")
                choice = get_menu_choice(MIN_CHOICE, MAX_CHOICE)
                if choice == ADD:
                    add(0)
                elif choice == FIND:
                    find(0)
                elif choice == CHANGE:
                    change(0)
                elif choice == DELETE:
                    delete(0)
                elif choice == SHOW_ALL:
                    show_all(0)
        elif choice == MAIN_DEPS:
            choice = 0
            while choice != EXIT:
                display_menu("Departments")
                choice = get_menu_choice(MIN_CHOICE, MAX_CHOICE)
                if choice == ADD:
                    add(1)
                elif choice == FIND:
                    find(1)
                elif choice == CHANGE:
                    change(1)
                elif choice == DELETE:
                    delete(1)
                elif choice == SHOW_ALL:
                    show_all(1)
        elif choice == MAIN_STUDENTS:
            choice = 0
            while choice != EXIT:
                display_menu("Students")
                choice = get_menu_choice(MIN_CHOICE, MAX_CHOICE)
                if choice == ADD:
                    add(2)
                elif choice == FIND:
                    find(2)
                elif choice == CHANGE:
                    change(2)
                elif choice == DELETE:
                    delete(2)
                elif choice == SHOW_ALL:
                    show_all(2)


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


# mode: 0 Majors, 1 Departments, 2 Students
def find(mode):
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        if mode == 0:  # Majors
            search = input("Enter a name to find: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT RowID, Name FROM Majors WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            else:
                print("Entry not found.")
        elif mode == 1:  # Departments
            search = input("Enter a name to find: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT RowID, Name FROM Departments WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            else:
                print("Entry not found.")
        elif mode == 2:  # Students
            search = input("Enter a name to find: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT StudentID, Name, MajorID, DeptID FROM Students WHERE lower(Name) LIKE ?''',
                        (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 1, cur)
            else:
                print("Entry not found.")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


# mode: 0 Majors, 1 Departments, 2 Students
def change(mode):
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')  # turn on foreign keys support
        if mode == 0:  # Majors
            search = input("Enter major's name to change: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT MajorID, Name FROM Majors WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            if len(result) == 1:
                id_update = result[0][0]
                update_entry(cur, id_update, 0)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_update = input("Enter MajorID that need to be change: ")
                    if id_update.isdigit():
                        id_update = int(id_update)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT MajorID FROM Majors WHERE MajorID == ?''', (id_update,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            update_entry(cur, id_update, 0)
                            conn.commit()
                        else:
                            print("Wrong MajorID.")
                    else:
                        print("MajorID should be integer.")
            else:
                print("Entry was not found.")
        elif mode == 1:  # Departments
            search = input("Enter department's name to change: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT DeptID, Name FROM Departments WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            if len(result) == 1:
                id_update = result[0][0]
                update_entry(cur, id_update, 1)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_update = input("Enter DeptID that need to be change: ")
                    if id_update.isdigit():
                        id_update = int(id_update)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT DeptID FROM Departments WHERE DeptID == ?''', (id_update,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            update_entry(cur, id_update, 1)
                            conn.commit()
                        else:
                            print("Wrong DeptID.")
                    else:
                        print("DeptID should be integer.")
            else:
                print("Entry was not found.")
        elif mode == 2:  # Students
            search = input("Enter student's name to change: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT StudentID, Name, MajorID, DeptID FROM Students WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 1, cur)
            if len(result) == 1:
                id_update = result[0][0]
                update_entry(cur, id_update, 2)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_update = input("Enter StudentID that need to be change: ")
                    if id_update.isdigit():
                        id_update = int(id_update)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT StudentID FROM Students WHERE StudentID == ?''', (id_update,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            update_entry(cur, id_update, 2)
                            conn.commit()
                        else:
                            print("Wrong StudentID.")
                    else:
                        print("StudentID should be integer.")
            else:
                print("Entry was not found.")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


# mode: 0 Majors, 1 Departments, 2 Students
def delete(mode):
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')  # turn on foreign keys support
        if mode == 0:  # Majors
            search = input("Enter major's name to delete: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT MajorID, Name FROM Majors WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            if len(result) == 1:
                id_delete = result[0][0]
                delete_entry(cur, id_delete, 0)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_delete = input("Enter MajorID that need to be deleted: ")
                    if id_delete.isdigit():
                        id_delete = int(id_delete)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT MajorID FROM Majors WHERE MajorID == ?''', (id_delete,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            delete_entry(cur, id_delete, 0)
                            conn.commit()
                        else:
                            print("Wrong MajorID.")
                    else:
                        print("MajorID should be integer.")
            else:
                print("Entry was not found.")

        elif mode == 1:  # Departments
            search = input("Enter department's name to delete: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT DeptID, Name FROM Departments WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 0, cur)
            if len(result) == 1:
                id_delete = result[0][0]
                delete_entry(cur, id_delete, 1)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_delete = input("Enter DeptID that need to be deleted: ")
                    if id_delete.isdigit():
                        id_delete = int(id_delete)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT DeptID FROM Departments WHERE DeptID == ?''', (id_delete,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            delete_entry(cur, id_delete, 1)
                            conn.commit()
                        else:
                            print("Wrong DeptID.")
                    else:
                        print("DeptID should be integer.")
            else:
                print("Entry was not found.")

        elif mode == 2:  # Students
            search = input("Enter student's name to delete: ")
            search = '%' + search.lower() + '%'
            cur.execute('''SELECT StudentID, Name, MajorID, DeptID FROM Students WHERE lower(Name) LIKE ?''', (search,))
            result = cur.fetchall()
            if len(result) > 0:
                display_entry(result, 1, cur)
            if len(result) == 1:
                id_delete = result[0][0]
                delete_entry(cur, id_delete, 2)
                conn.commit()
            elif len(result) > 1:  # if there were more than one entry found
                loop_flag = 0
                while loop_flag < 2:
                    id_delete = input("Enter StudentID that need to be deleted: ")
                    if id_delete.isdigit():
                        id_delete = int(id_delete)
                        loop_flag += 1
                        # check if entered RowID is in table
                        cur.execute('''SELECT StudentID FROM Students WHERE StudentID == ?''', (id_delete,))
                        result_id = cur.fetchall()
                        if len(result_id) == 1:  # found one RowID, that user has entered
                            loop_flag += 1
                            delete_entry(cur, id_delete, 2)
                            conn.commit()
                        else:
                            print("Wrong StudentID.")
                    else:
                        print("StudentID should be integer.")
            else:
                print("Entry was not found.")

    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


# mode: 0 for Majors, Departments, 1 for Students
def show_all(mode):
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        if mode == 0:  # Majors
            cur.execute('''SELECT MajorID, Name FROM Majors''')
            result = cur.fetchall()
            display_entry(result, 0, cur)
        elif mode == 1:  # Departments
            cur.execute('''SELECT DeptID, Name FROM Departments''')
            result = cur.fetchall()
            display_entry(result, 0, cur)
        elif mode == 2:  # Students
            cur.execute('''SELECT StudentID, Name, MajorID, DeptID FROM Students''')
            result = cur.fetchall()
            display_entry(result, 1, cur)
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


# mode: 0 for Majors, Departments, 1 for Students
def display_entry(result, mode, cur):
    if mode == 0:  # Majors, Departments
        # variables to print header
        id = 'ID'
        n = 'Name'
        print(f"{id:<3} {n:<12}")
        print("----------------------")
        for entry in result:
            print(f"{entry[0]:<3} {entry[1]:<12}")
    if mode == 1:  # Students
        # variables to print header
        id = 'ID'
        n = 'Name'
        maj_header = 'Major'
        dep_header = 'Department'
        print(f"{id:<3} {n:<12} {maj_header:<12} {dep_header:<12}")
        print("--------------------------------------------------")
        for entry in result:
            # get major's name from Majors table
            cur.execute('''SELECT Name FROM Majors WHERE MajorID == ?''', (entry[2],))
            major = cur.fetchone()[0]
            # get department's name from Departments table
            cur.execute('''SELECT Name FROM Departments WHERE DeptID == ?''', (entry[3],))
            dept = cur.fetchone()[0]
            print(f"{entry[0]:<3} {entry[1]:<12} {major:<12} {dept:<12}")


# mode: 0 for Majors, 1 for Departments, 2 for Students
def update_entry(cur, id_update, mode):
    if mode == 0:  # Majors
        name = input("Enter new major's name or just press 'Enter' to save previous: ")
        if len(name) > 1:  # if name was entered
            cur.execute('''UPDATE Majors SET Name = ? WHERE MajorID == ?''', (name, id_update))
            print(f"{name} was added.")
        else:
            print("Major was not changed.")
    elif mode == 1:  # Departments
        name = input("Enter new department's name or just press 'Enter' to save previous: ")
        if len(name) > 1:  # if name was entered
            cur.execute('''UPDATE Departments SET Name = ? WHERE DeptID == ?''', (name, id_update))
            print(f"{name} was added.")
        else:
            print("Department was not changed.")
    elif mode == 2:  # Students
        name = input("Enter new student's name or just press 'Enter' to save previous: ")
        cur.execute('''SELECT MajorID, Name FROM Majors''')
        result = cur.fetchall()
        print("--- Majors ---")
        display_entry(result, 0, cur)
        # validation loop for integer MajorID
        loop_flag = True
        while loop_flag:
            majorid = input("Enter MajorID for student from above: ")
            if majorid.isdigit():
                majorid = int(majorid)
                loop_flag = False
        cur.execute('''SELECT DeptID, Name FROM Departments''')
        result = cur.fetchall()
        print("--- Departments ---")
        display_entry(result, 0, cur)
        # validation loop for integer DeptID
        loop_flag = True
        while loop_flag:
            deptid = input("Enter DeptID for student from above: ")
            if deptid.isdigit():
                deptid = int(deptid)
                loop_flag = False
        if len(name) > 1:  # if name was entered
            try:
                cur.execute('''UPDATE Students SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID == ?''',
                            (name, majorid, deptid, id_update))
                print(f"{name} was added.")
            except sqlite3.Error as err:
                print(err)
        else:
            print(f"Entry was not changed.")


# mode: 0 for Majors, 1 for Departments, 2 for Students
def delete_entry(cur, id_delete, mode):
    if mode == 0:  # Majors
        try:
            cur.execute('''DELETE FROM Majors WHERE MajorID == ?''', (id_delete,))
            print("Entry was deleted.")
        except sqlite3.Error as err:
            print(err)

    elif mode == 1:  # Departments
        try:
            cur.execute('''DELETE FROM Departments WHERE DeptID == ?''', (id_delete,))
            print("Entry was deleted.")
        except sqlite3.Error as err:
            print(err)

    elif mode == 2:  # Students
        try:
            cur.execute('''DELETE FROM Students WHERE StudentID == ?''', (id_delete,))
            print("Entry was deleted.")
        except sqlite3.Error as err:
            print(err)


if __name__ == '__main__':
    main()
