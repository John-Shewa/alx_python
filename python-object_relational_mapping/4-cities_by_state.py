#!/usr/bin/python3
""" This is a script that lists all cities
from the database hbtn_0e_4_usa."""
if __name__ == '__main__':
    import sys
    import MySQLdb

    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connect.cursor()

    cur.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC""")

    for row in cur.fetchall():
        print(row)

    cur.close()
    connect.close()
