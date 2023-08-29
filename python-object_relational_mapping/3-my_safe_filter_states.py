#!/usr/bin/python3
""" This is a script that takes in an argument
and displays all values in the states table of
where name matches the argument."""
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
        """SELECT * FROM states WHERE `name` = %(user)s
        ORDER BY states.id ASC""", {'user': user})

    for row in cur.fetchall():
        print(row)

    cur.close()
    connect.close()
