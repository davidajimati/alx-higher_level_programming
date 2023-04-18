#!/usr/bin/python3
"""
This module takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    con = db.cursor()
    con.execute("SELECT * FROM states WHERE name=%s ORDER\
                     BY states.id ASC", (argv[4],))
    items = con.fetchall()
    for item in items:
        print(item)
