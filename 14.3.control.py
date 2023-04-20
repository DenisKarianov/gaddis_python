# study SQLite

import sqlite3


def main():
    # connect database
    conn = sqlite3.connect('chocolate.db')
    # make cursor
    cur = conn.cursor()
    # update instruction
    cur.execute('''UPDATE Products SET RetailPrice = 4.99 WHERE Description LIKE "%shaving%"''')
    # delete instruction
    cur.execute('''DELETE FROM Products WHERE RetailPrice > 4.00''')

    conn.commit()
    conn.close()


# call main function
if __name__ == '__main__':
    main()
