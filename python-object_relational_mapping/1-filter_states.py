#!/usr/bin/python3
""" This is a script that prints all
states with a name starting with N
from the database hbtn_0e_0_usa """

import sys
import MySQLdb

__name__ = '__main__'
connect = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
cur = connect.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
[print(state) for state in cur.fetchall() if state[1][0] == "N"]
