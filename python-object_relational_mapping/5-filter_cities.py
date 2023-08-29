#!/usr/bin/python3
""" This is a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connect.cursor()
    user = sys.argv[4].strip("'")
    cur.execute(
        """ SELECT cities.name
        FROM cities
        WHERE cities.state_id in (SELECT states.id
        FROM states
        WHERE states.name= '{}')
        ORDER BY cities.id ASC""".format(user))
    city = cur.fetchall()
    compiled = []
    for i in city:
        j = [compiled.append(N) for N in i]
    print(", ".join(compiled))

    cur.close()
    connect.close()
