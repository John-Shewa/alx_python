#!/usr/bin/python3
""" This is a script that takes in an argument
and displays all values in the states table of
where name matches the argument."""

import sys
import MySQLdb

__name__ = '__main__'
connect = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
cur = connect.cursor()
cur.execute(
    """SELECT * FROM states WHERE BINARY `name` = "{}" ORDER BY id ASC"""
    .format(sys.argv[4].strip("'")))

for row in cur.fetchall():
    print(row)

cur.close()
connect.close()
