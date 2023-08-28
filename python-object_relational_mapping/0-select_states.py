#!/usr/bin/python3
"""This script lists all states from database"""
import MySQLdb


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

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 password=password,
                                 database=database)

    query = "SELECT * FROM states ORDER BY id ASC"
    result = connection.query(query)

    for row in result:
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
