# program to work with cities.db
import sqlite3

# constants
MIN_CHOICE = 1
MAX_CHOICE = 8
INCREASE_ORDER = 1
DESCENT_ORDER = 2
NAME_ORDER = 3
TOTAL_POPULATION = 4
AVG_POPULATION = 5
MOST_CITY = 6
LEAST_CITY = 7
EXIT = 8


def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()
        if choice == INCREASE_ORDER:
            order(0)
        elif choice == DESCENT_ORDER:
            order(1)
        elif choice == NAME_ORDER:
            order(2)
        elif choice == TOTAL_POPULATION:
            total_pop()
        elif choice == AVG_POPULATION:
            avg_pop()
        elif choice == MOST_CITY:
            most_city()
        elif choice == LEAST_CITY:
            least_city()


def display_menu():
    print("\n--- City database menu ---")
    print("1. Show cities in increasing order.")
    print("2. Show cities in descending order.")
    print("3. Show cities in alphabet order.")
    print("4. Show total population in all cities.")
    print("5. Show average population among all cities.")
    print("6. Show most populated city.")
    print("7. Show least populated city.")
    print("8. Quit program.")


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


def order(d):  # if d == 0 increasing order, elif d == 1 descending order, elif d == 2 alphabet order
    conn = None
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()
        if d == 0:
            cur.execute('''SELECT CityName FROM Cities ORDER BY Population''')
        elif d == 1:
            cur.execute('''SELECT CityName FROM Cities ORDER BY Population DESC''')
        elif d == 2:
            cur.execute('''SELECT CityName FROM Cities ORDER BY CityName''')
        for city in cur.fetchall():
            print(city[0])
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


def total_pop():
    conn = None
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()
        cur.execute('''SELECT SUM(Population) FROM Cities''')
        print(f"Total population: {cur.fetchone()[0]:.0f}")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


def avg_pop():
    conn = None
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()
        cur.execute('''SELECT AVG(Population) FROM Cities''')
        print(f"Average population: {cur.fetchone()[0]:.0f}")
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


def most_city():
    conn = None
    try:
        conn = sqlite3.connect('cities.db')
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
        conn = sqlite3.connect('cities.db')
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
