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

    search_query = (argv[4] + '%')
    sql_query = """SELECT * FROM states WHERE name LIKE %s ORDER
                     BY states.id ASC""".format(search_query, )
    cur = db.cursor()
    cur.execute(sql_query)
    items = cur.fetchall()

    for item in items:
        print(item)
