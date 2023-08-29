#!/usr/bin/python3
"""This script lists all states from database"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3])

    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    connect.close()
