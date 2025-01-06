#!/usr/bin/python3
"""
Module to connect to a MySQL database and retrieve all values in `states`
where `name` matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = "SELECT * FROM `states`WHERE BINARY name = %s ORDER BY `id` ASC"
    cur.execute(query, (search,))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
