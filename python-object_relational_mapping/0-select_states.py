#!/usr/bin/python3
"""This script lists all states from database"""
import MySQLdb as DB


def main():
    """ 
    Lists all states from hbtn_0e_0_usa

    Args:
        username: The user name for Mysql
        Password: The pass word of Mysql
        database: The name of the database 
    """

    username = input("user name:")
    password = input("Enter password:")
    database = input("Enter database name:")

    db_connect = DB.connect(host="localhost", port=3306,
                            user="root", passwd="root", db="my_db")

    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor:
        print(row)

    cursor.close()
    db_connect.close()


if __name__ == "__main__":
    main()
