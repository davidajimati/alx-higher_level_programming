#!/usr/bin/python3
"""
This module lists all states
    with a name starting with N (upper N) from
    the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name BINARY
                LIKE 'N%' ORDER BY states.id ASC""")
    output = cur.fetchall()
    for state in output:
        print(state)
