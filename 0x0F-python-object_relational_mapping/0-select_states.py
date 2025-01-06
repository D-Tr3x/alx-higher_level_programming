#!/usr/bin/python3
"""
Module to connect a MySQL database and retrieve all states
from the `states` table
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    conn.close()
