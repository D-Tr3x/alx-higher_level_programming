#!/usr/bin/python3
"""
Module to connect to a MySQL database and retrieve all states starting with 'N'
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
