# study SQLite

import sqlite3


def main():
    # connect to database
    conn = sqlite3.connect('database.db')
    # get cursor
    cur = conn.cursor()
    # add table
    cur.execute('''CREATE TABLE IF NOT EXISTS Book (BookID INTEGER PRIMARY KEY NOT NULL,
               Publisher TEXT, Author TEXT, Page INTEGER, ISBN TEXT)''')
    # remove table
    cur.execute('DROP TABLE IF EXISTS Book')
    # save changes
    conn.commit()
    # close database
    conn.close()

    # connect 2nd database
    conn2 = sqlite3.connect('inventory.db')
    # make cursor
    cur2 = conn2.cursor()
    # add table
    cur2.execute(
        '''CREATE TABLE IF NOT EXISTS Inventory (ItemID INTEGER PRIMARY KEY NOT NULL, ItemName TEXT, Price REAL)''')
    # add lines
    cur2.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                VALUES (10, 'Circular saw', 199.99)''')
    cur2.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES ('Chisel', 8.99)''')
    # add lines by parametric query
    name_input = 'Flamethrower'
    price_input = 600
    cur2.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES (?, ?)''', (name_input, price_input))
    conn2.commit()
    conn2.close()


# call main function
if __name__ == '__main__':
    main()
