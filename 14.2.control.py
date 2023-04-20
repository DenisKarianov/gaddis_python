# study SQLite

import sqlite3


def main():
    # connect database
    conn = sqlite3.connect('inventory.db')
    # make cursor
    cur = conn.cursor()
    # add table
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS Inventory (ProductName TEXT, QtyOnHand INTEGER, Cost REAL)''')
    # some SELECT instructions
    cur.execute('''SELECT * FROM Inventory''')
    cur.execute('''SELECT ProductName FROM Inventory''')
    cur.execute('''SELECT ProductName, QtyOnHand FROM Inventory''')
    cur.execute('''SELECT ProductName FROM Inventory WHERE ProductName < 17.00''')
    cur.execute('''SELECT * FROM Inventory WHERE ProductName LIKE "%ZZ"''')
    conn.commit()
    conn.close()


# call main function
if __name__ == '__main__':
    main()
