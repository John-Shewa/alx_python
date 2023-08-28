#!/usr/bin/python3
"""This script lists all states from database"""
import MySQLdb as DB


def main(username, password, database):
    """ 
    Lists all states from hbtn_0e_0_usa

    Args:
        username: The user name for Mysql
        Password: The pass word of Mysql
        database: The name of the database 
    """

    db_connect = DB.connect(host="localhost",
                                 port=3306,
                                 user="root",
                                 passwd="root",
                                 db="my_db",
                                 charset="utf8")

    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY id ASC")
    results = db_cursor.fetchall()

    for row in results:
        print(row[1])

    cursor.close()
    connection.close()


if __name__ == "__main__":

    username = input("user name:")
    password = input("Enter password:")
    database = input("Enter database name:")

    main(username, password, database)
