#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    search = argv[4]
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                 ON cities.state_id = states.id WHERE \
                states.name = %s ORDER BY cities.id ASC", (search,))

    result = cur.fetchall()
    print(", ".join([row[0] for row in result]))
