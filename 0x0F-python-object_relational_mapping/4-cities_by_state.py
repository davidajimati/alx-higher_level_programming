#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name AS city_name, states.name \
                AS state_name FROM cities JOIN states ON \
                states.id = cities.state_id")

    result = cur.fetchall()
    for item in result:
        print(item)
